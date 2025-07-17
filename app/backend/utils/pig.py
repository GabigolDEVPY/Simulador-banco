from ..utils.bd_connect import BD_execute
from flask import session
from datetime import datetime
from ..utils.cliente import Cliente

class Pig:
    @staticmethod
    def return_pigs():
        pigs = BD_execute.execute_comand("SELECT * FROM pigs WHERE user_id = %s", session["user_id"])
        return pigs
    
    @staticmethod
    def criar_pig():
        BD_execute