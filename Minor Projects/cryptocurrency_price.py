import requests

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    print("Live Cryptocurrency Prices")
    print("--------------------------")
    print("Bitcoin :", "$", data["bitcoin"]["usd"])
    print("Ethereum:", "$", data["ethereum"]["usd"])

else:
    print("Failed to fetch data.")