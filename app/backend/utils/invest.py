from ..utils.bd_connect import BD_execute
from flask import session
from ..utils.cliente import Cliente

class Criptos():
    def __init__(self, *args, **kwargs):
        self.id = args
        self.dolar = args
        self.ethereum = args
        self.bitcoin = args
        
        
def Create_class():
    data = BD_execute.execute_comand("SELECT * FROM invest WHERE user_id = %s", session["user_id"])
    print(data)
    criptos =Criptos()        