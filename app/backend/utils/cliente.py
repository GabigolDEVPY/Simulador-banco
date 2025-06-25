from ..utils.bd_connect import BD_execute

class Cliente():
    @staticmethod
    def login(dados):
        comand = "SELECT * FROM users WHERE user_login = %s AND user_password = %s"
        result = BD_execute.execute_comand(comand, dados['login'], dados['senha'])
        return result

    @staticmethod
    def register(dados):
        comand = "INSERT INTO users (user_name, user_login, user_password, chave_pix) VALUES (%s, %s, %s, %s)"
        result = BD_execute.execute_comand(comand, dados['nome'], dados['login'], dados['senha'], dados['chave'])
        return result

dados = {
    "nome": "gabriel",
    "login": "gabigol",
    "senha": "12345678",
    "chave": "gabriel1234"
}

Cliente.register(dados)