import requests

class BitcoinAPI:
    def __init__(self):
        self.api_url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR'
      
    def get(self):
        response = requests.get(self.api_url) 
    
        price = response.json()["USD"]["price"]
        value= response.json()["JPY"]
        amount= response.json()["EUR"]

        print(price)
        print(value)
        print(amount)

      
    
    




       