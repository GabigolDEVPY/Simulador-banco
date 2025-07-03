from ..utils.bd_connect import BD_execute
from flask import session

class Payment:
    @staticmethod
    def pix_sender_verify(dados):
        validate_valor = BD_execute.execute_comand("SELECT user_found FROM users WHERE user_login = %s", session['login'])
        if float((validate_valor[0])['user_found']) >= float(dados['valor']):
            validate_user = BD_execute.execute_comand("SELECT user_name, chave_pix, FROM users WHERE chave_pix = %s", dados['chave'])
            if validate_user:
                return validate_user
            return 2
        return 1
    
    def pix_sender(dados):
        result = BD_execute.execute_comand("UPDATE users SET user_found = user_found + %s, user_notifications = user_notifications + %s", dados['valor'], 1)
        return



    
