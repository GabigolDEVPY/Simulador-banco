from flask import Blueprint, render_template, request, jsonify, make_response
from ..utils.cliente import Cliente
login_register_bp = Blueprint('login_register', __name__,template_folder='../../templates/login-register')



@login_register_bp.route('/', methods=["GET"])
def return_home():
    return render_template('login.html')


@login_register_bp.route('/login', methods=["GET"])
def return_login():
    dados = request.args.to_dict()
    if dados:
        result = Cliente.login(dados)
        if result:
            return render_template('home.html')
        return render_template('login.html', error="Usuário ou senha inválidos")
    return jsonify('Dados Inválidos'), 404


@login_register_bp.route('/register', methods=["GET"])
def return_register_page():
    return render_template('register.html')