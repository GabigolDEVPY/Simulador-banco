import requests

class Get_value():

    @staticmethod
    def puxar_cripto(url):
        url = url
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
    def puxar_dolar():
        url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()['USDBRL']
            print(dados)
            dados = {
                "preco": dados['bid'],
                "maximo": dados['high'],
                "minimo": dados['low']
            }
            return dados


