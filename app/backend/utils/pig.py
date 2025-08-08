from ..utils.bd_connect import BD_execute
from flask import session
from datetime import datetime
from ..utils.cliente import Cliente


class Pig:
    @staticmethod
    def return_pigs():
        pigs = BD_execute.execute_comand("SELECT * FROM pigs WHERE user_id = %s", session["user_id"])
        num_caixinhas = len(pigs) if pigs else 0
        return pigs, num_caixinhas
    
    @staticmethod
    def return_pig(id):
        return (BD_execute.execute_comand("SELECT * FROM pigs WHERE user_id = %s AND pig_id = %s", session["user_id"], id))[0]
    
    @staticmethod
    def return_bruto():
        total_bruto = (BD_execute.execute_comand("SELECT SUM(total_bruto) AS total FROM pigs WHERE user_id = %s", session['user_id']))[0]["total"]
        return total_bruto if total_bruto else 0
    
    @staticmethod
    def criar_pig(dados):
        values = (session["user_id"], dados["meta"], 0, dados["imagem"], dados["nome"])
        BD_execute.execute_comand("INSERT INTO pigs (user_id, meta_pig, total_bruto, image_pig, nome_pig) VALUES (%s, %s, %s, %s, %s)", *values)

    @staticmethod
    def guardar_pig(dados, pig_id):
        value_cliente = Cliente.value_user()
        validate = Cliente.validate_senha(dados["senha"])
        if validate:
            if value_cliente >= float((dados)["value"]):
                comand = BD_execute.execute_comand("UPDATE pigs SET total_bruto = total_bruto + %s WHERE pig_id = %s AND user_id = %s", float((dados)["value"]), pig_id, session['user_id'])
                Cliente.discount_user(float(dados["value"]))
                return
            return 0    
        return 2
        
    @staticmethod
    def resgatar_pig(dados, pig_id):
        validate = Cliente.validate_senha(dados["senha"])
        total_bruto = BD_execute.execute_comand("SELECT total_bruto FROM pigs WHERE pig_id = %s AND user_id = %s", pig_id, session["user_id"])[0]["total_bruto"]
        print("totalllllllllll", total_bruto)
        if total_bruto >= float(dados["value"]):
            if validate:
                print("validadoooooooooooooooooooooooooo")
                comand = BD_execute.execute_comand("UPDATE pigs SET total_bruto = total_bruto - %s WHERE pig_id = %s AND user_id = %s", float((dados)["value"]), pig_id, session['user_id'])
                Cliente.acrescent_user(float(dados["value"]))
                return
            return 0    
        return 1
    
    @staticmethod
    def deletar_pig(id):
        result = BD_execute.execute_comand("DELETE FROM pigs WHERE pig_id = %s AND user_id = %s", id, session["user_id"])    
        print(result)
        return
    

