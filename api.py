import requests
import json

base_key = "USD"
sym_key = "RUB"
amount = 100
API_KEY = 'ePVMJVY9kMjos0FVajjBOBtaCuEar9BR'

url = f"https://api.apilayer.com/exchangerates_data/convert?to={sym_key}&from={base_key}&amount={amount}"

payload = {}
headers= {
  "apikey": API_KEY
}

response = requests.request("GET", url, headers=headers, data = payload)

resp = json.loads(response.content)
new_price = resp['result']

print(round(new_price, 2))
