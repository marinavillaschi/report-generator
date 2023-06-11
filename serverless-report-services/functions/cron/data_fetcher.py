import json
from decouple import config

from services import api_requester


def lambda_handler(event, context):
    """ Lambda function to fetch data from external API and upload it to S3 """

    print(f"Attempting to fetch data from **coingecko** API")

    try:
        coins_marked_data = api_requester.get_coins_market_data()
        coins_marked_data = coins_marked_data.json()


    except:
        raise Exception({
            'statusCode': 500,
            'body': json.dumps(f"FAILED making API request"),
        })


    print(f"got {len(coins_marked_data)} coin market data successfully")
