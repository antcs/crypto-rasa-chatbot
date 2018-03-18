def call(currency):
    import requests
    response = requests.get('https://api.coinmarketcap.com/v1/ticker/' + currency)
    json = response.json()
    return json[0]['price_usd']
