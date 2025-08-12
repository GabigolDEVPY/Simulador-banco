from ..utils.bd_connect import BD_execute
from flask import session
from ..utils.cliente import Cliente

class Criptos():
    def __init__(self, data):
        self.id = data["id"]
        self.dolar = data["dolar_invest"]
        self.ethereum = data["ethereum_invest"]
        self.bitcoin = data["bitcoin_invest"]
    
    def add_cripto(self, dados : dict) -> int:
        dados = dados
        cripto = str(dados["cripto"]+"_invest")
        value_user = Cliente.value_user()
        if float(value_user) >= float(dados["valor"]):
            result = BD_execute.execute_comand(f"UPDATE invest SET {cripto} = {cripto} + %s WHERE user_id = %s", dados["quantidade"], session["user_id"])
            Cliente.discount_user(float(dados["valor"]))
            return
        return 1
    
    def remove_cripto(self, dados : dict) -> int:
        dados = dados
        cripto = str(dados["cripto"]+"_invest")
        value_cripto = float(Create_class().__dict__.get(dados["cripto"]))
        print("valorrrrr criptos",value_cripto)
        if value_cripto >= float(dados["quantidade"]):
            result = BD_execute.execute_comand(f"UPDATE invest SET {cripto} = {cripto} - %s WHERE user_id = %s", dados["quantidade"], session["user_id"])
            Cliente.acrescent_user(float(dados["valor"]))
            return
        return 1

def Create_class():
    data = BD_execute.execute_comand("SELECT * FROM invest WHERE user_id = %s", session["user_id"])[0]
    criptos =Criptos(data)        
    return criptos