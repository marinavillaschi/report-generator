import json
from decouple import config
from datetime import date

from services import api_requester, s3_uploader

BUCKET = config("BUCKET")


# def lambda_handler(event, context):
def lambda_handler():
    """ Lambda function to fetch data from external API and upload it to S3 """

    print("Attempting to fetch data from coingecko API")

    try:
        coins_marked_data = api_requester.get_coins_market_data()
        coins_marked_data = coins_marked_data.json()

    except:
        raise Exception({
            'statusCode': 500,
            'body': json.dumps("FAILED making API request"),
        })


    print(f"got {len(coins_marked_data)} coin market data successfully")

    try:
        response_date = s3_uploader.upload_to_s3(BUCKET, f"raw/{str(date.today())}/coins_market_data.json", coins_marked_data)
    except:
        raise Exception({
            'statusCode': 500,
            'body': json.dumps(f"FAILED uploading data to S3 on {response_date}"),
        })

    

if __name__ == "__main__":
    lambda_handler()
