import pandas as pd
from decouple import config
from datetime import date

from services import api_requester

LAKE_BUCKET_NAME = config("LAKE_BUCKET_NAME")
MARKET_CATEGORY = config("MARKET_CATEGORY")


def lambda_handler(event, context):
    """ Lambda function to fetch data from external API and upload it to S3 """

    print("Attempting to fetch data from coingecko API")

    try:
        coins_market_data = api_requester.get_coins_market_data(vs_currency="USD", category=MARKET_CATEGORY)
        coins_market_data = coins_market_data.json()

    except Exception as e:
        raise Exception({
            "statusCode": 500,
            "body": "FAILED making API request",
            "error": e
        })

    print(f"got {len(coins_market_data)} coin market data successfully")
    print("Ready to upload it to S3!")

    try:
        df = pd.DataFrame(coins_market_data)
        s3_filepath = f"s3://{LAKE_BUCKET_NAME}/raw/coins_market_data/{MARKET_CATEGORY}/{str(date.today())}.csv"

        df.to_csv(s3_filepath, index=False)
        print(f"file {s3_filepath.split('/')[-1]} uploaded to S3 successfully!")

    except Exception as e:
        raise Exception({
            "statusCode": 500,
            "body": "FAILED uploading API data to S3",
            "error": e
        })
