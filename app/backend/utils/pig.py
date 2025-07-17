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
    def criar_pig(dados):
        values = (session["user_id"], dados["meta"], 0, dados["imagem"], dados["nome"])
        BD_execute.execute_comand("INSERT INTO pigs (user_id, meta_pig, total_bruto, image_pig, nome_pig) VALUES (%s, %s, %s, %s, %s)", values)