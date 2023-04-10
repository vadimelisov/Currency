import requests
import json
from config import exchanges

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")
        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена!")

        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')
        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')


        API_KEY = 'ePVMJVY9kMjos0FVajjBOBtaCuEar9BR'

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={sym_key}&from={base_key}&amount={amount}"

        payload = {}
        headers = {
            "apikey": API_KEY
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        resp = json.loads(response.content)
        new_price = resp['result']

        return round(new_price, 2)