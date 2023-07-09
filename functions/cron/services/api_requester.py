import requests
from decouple import config

API_URL = config("API_URL")

def get_coins_market_data(vs_currency: str, category: str = None, coin_ids: str = None):

    url = API_URL


    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "price_change_percentage": "1h, 24h, 7d, 30d, 90d, 1y",
        "per_page": 10,
        "category": category,
        "ids": coin_ids,
    }

    response = requests.get(url, params=params)
    return response
