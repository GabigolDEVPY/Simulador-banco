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
        
        
        
def Create_class():
    data = BD_execute.execute_comand("SELECT * FROM invest WHERE user_id = %s", session["user_id"])[0]
    criptos =Criptos(data)        
    return criptos