import requests

class Get_value():

    @staticmethod
    def puxar_bitcoin():
        url = 'https://api.coingecko.com/api/v3/coins/bitcoin'
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()
            dados = {
                "preco": float(dados['market_data']['current_price']['brl']),
                "maximo": float(dados['market_data']['high_24h']['brl']),
                "minimo": float(dados['market_data']['low_24h']['brl'])
            }
            return dados
        
    @staticmethod
    def puxar_ethereum():
        url = 'https://api.coingecko.com/api/v3/coins/ethereum'
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()
            dados = {
                "preco": dados['market_data']['current_price']['brl'],
                "maximo": dados['market_data']['high_24h']['brl'],
                "minimo": dados['market_data']['low_24h']['brl']
            }
            return dados
