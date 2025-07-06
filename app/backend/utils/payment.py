from ..utils.bd_connect import BD_execute
from flask import session

class Payment:
    @staticmethod
    def pix_sender_verify(dados):
        if dados['chave_pix'] == session["chave_pix"]:
            return 3
        if "validado" in dados:
                validate_senha = (BD_execute.execute_comand("SELECT user_password FROM users WHERE user_login = %s", session["login"]))[0]['user_password']
                if validate_senha == dados["user_password"]:
                    result = BD_execute.execute_comand("UPDATE users SET user_found = user_found + %s, user_notifications = user_notifications + %s WHERE chave_pix = %s", dados['valor'], 1, dados["chave_pix"])
                    BD_execute.execute_comand("UPDATE users SET user_found = user_found - %s WHERE user_login = %s", dados['valor'], session['login'])
                    return
                return 4
        validate_valor = BD_execute.execute_comand("SELECT user_found FROM users WHERE user_login = %s", session['login'])
        if float((validate_valor[0])['user_found']) >= float(dados['valor']):
            validate_user = BD_execute.execute_comand("SELECT user_name, chave_pix FROM users WHERE chave_pix = %s", dados['chave_pix'])
            if validate_user:
                return validate_user
            return 2
        return 1
    




