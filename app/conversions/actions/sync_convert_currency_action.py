import requests
from ...config import settings
from fastapi import HTTPException

def handle(from_currency: str, to_currencies: str, price: float) -> dict:
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currencies}&apikey={settings.alpha_vantage_api}'
    try:
        response = requests.get(url)
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
    data = response.json()
    if ("Realtime Currency Exchange Rate" not in data):
        raise HTTPException(400, "Realtime Currency NOT in response!")
    exchange_rate = float(data ["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    return {to_currencies : (price*exchange_rate)}