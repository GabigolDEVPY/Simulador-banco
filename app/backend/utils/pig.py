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
    def return_pig(id):
        pig = BD_execute.execute_comand("SELECT * FROM pigs WHERE user_id = %s AND pig_id = %s", session["user_id"], id)
        return pig[0]
    
    @staticmethod
    def return_bruto():
        total_bruto = (BD_execute.execute_comand("SELECT SUM(total_bruto) AS total FROM pigs WHERE user_id = %s", session['user_id']))[0]["total"]
        print(total_bruto)
        return total_bruto
    
    @staticmethod
    def criar_pig(dados):
        values = (session["user_id"], dados["meta"], 0, dados["imagem"], dados["nome"])
        BD_execute.execute_comand("INSERT INTO pigs (user_id, meta_pig, total_bruto, image_pig, nome_pig) VALUES (%s, %s, %s, %s, %s)", *values)

    @staticmethod
    def guardar_pig(valor, pig_id):
        value_cliente = Cliente.value_user()
        if value_cliente >= float(valor):
            comand = BD_execute.execute_comand("UPDATE pigs SET total_bruto = total_bruto + %s WHERE pig_id = %s AND user_id = %s", valor, pig_id, session['user_id'])
            return
        return 0    
        
    @staticmethod
    def deletar_pig(id):
        result = BD_execute.execute_comand("DELETE FROM pigs WHERE pig_id = %s AND user_id = %s", id, session["user_id"])    
        print(result)
        return
