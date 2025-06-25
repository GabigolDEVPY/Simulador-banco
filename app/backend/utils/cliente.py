from ..utils.bd_connect import BD_execute

class Cliente():
    @staticmethod
    def login(dados):
        comand = "SELECT * FROM users WHERE user_login = %s AND user_password = %s"
        result = BD_execute.execute_comand(comand, dados['login'], dados['senha'])
        return result
