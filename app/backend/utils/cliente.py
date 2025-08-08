from ..utils.bd_connect import BD_execute
from flask import session

class Cliente():
    @staticmethod
    def login(dados):
        if "login" in session:
            print(session['login'])
            dados = BD_execute.execute_comand("SELECT * FROM users WHERE user_login = %s", session['login'])
            return dados[0]
        
        comand = "SELECT * FROM users WHERE user_login = %s AND user_password = %s"
        result = BD_execute.execute_comand(comand, dados['login'], dados['senha'])
        if result:
            dados = BD_execute.execute_comand("SELECT * FROM users WHERE user_login = %s", dados['login'])
            return dados
        return None
    
    @staticmethod
    def register(dados):
        comand = "INSERT INTO users (user_name, user_login, user_password, chave_pix) VALUES (%s, %s, %s, %s)"
        try:
            result = BD_execute.execute_comand(comand, dados['nome'], dados['login'], dados['senha'], dados['chave'])
        except Exception: 
            return None
        return result

    @staticmethod
    def notify():
        dados = BD_execute.execute_comand("SELECT * FROM user_notifications WHERE user_id = %s", session["user_id"])
        if dados:
            return dados
        return None
    
    @staticmethod
    def zerar_notifys(user_id):
        result = BD_execute.execute_comand("UPDATE users SET user_notifications = 0 WHERE user_id = %s", user_id)

    @staticmethod
    def create_notify(user_id, title_notify, subtitle_notify):
        dados = BD_execute.execute_comand("INSERT INTO user_notifications (user_id, title_notify, subtitle_notify) VALUES (%s, %s, %s)", user_id, title_notify, subtitle_notify)
        return
    
    @staticmethod
    def create_history(user_id, title_history, subtitle_history):
        history = BD_execute.execute_comand("INSERT INTO user_history (user_id, title_history, subtitle_history) VALUES (%s, %s, %s)", user_id, title_history, subtitle_history)

    @staticmethod
    def history():
        dados = BD_execute.execute_comand("SELECT * FROM user_history WHERE user_id = %s", session["user_id"])
        return dados

    @staticmethod
    def value_user():
        value = (BD_execute.execute_comand("SELECT user_found FROM users WHERE user_id = %s", session['user_id']))[0]['user_found']
        return value
    
    @staticmethod
    def discount_user(value):
        BD_execute.execute_comand("UPDATE users SET user_found = user_found - %s WHERE user_id = %s", value, session["user_id"])
        return
    
    @staticmethod
    def acrescent_user(value):
        BD_execute.execute_comand("UPDATE users SET user_found = user_found + %s WHERE user_id = %s", value, session["user_id"])
        return

    @staticmethod
    def validate_senha(senha):
        if senha == BD_execute.execute_comand("SELECT user_password FROM users WHERE user_id = %s", session["user_id"])[0]["user_password"]:
            return 1
        return None
