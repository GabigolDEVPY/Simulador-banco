from ..utils.bd_connect import BD_execute
from flask import session
from ..utils.cliente import Cliente

class Criptos():
    def __init__(self, data):
        self.id = data["id"]
        self.dolar = data["dolar_invest"]
        self.ethereum = data["ethereum_invest"]
        self.bitcoin = data["bitcoin_invest"]
        self.total = sum([self.ethereum, self.bitcoin, self.dolar])
    
    def add_cripto(self, dados : dict) -> int:
        dados = {'quantidade': '1000', 'valor': 0.0015431574853940143, 'cripto': 'bitcoin'}
        cripto = str(dados["cripto"]+"_invest")
        criptos = {"dolar": self.dolar, "ethereum": self.ethereum, "bitcoin": self.bitcoin}
        value_user = Cliente.value_user()
        if float(value_user) >= float(dados["valor"]):
            result = BD_execute.execute_comand(f"UPDATE invest SET {cripto} = %s WHERE user_id = %s", dados["valor"], session["user_id"])
            print(result)
        return
        

        
def Create_class():
    data = BD_execute.execute_comand("SELECT * FROM invest WHERE user_id = %s", session["user_id"])[0]
    criptos =Criptos(data)        
    return criptos