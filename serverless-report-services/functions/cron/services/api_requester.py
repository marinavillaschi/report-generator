import requests
from decouple import config

API_URL = config("API_URL")

def get_coins_market_data():

    url = API_URL


    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "price_change_percentage": "1h, 24h, 7d, 30d, 90d, 1y",
        "category": "artificial-intelligence",
    }

    response = requests.get(url, params=params)
    return response
