from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from ..utils.cliente import Cliente
login_register_bp = Blueprint('login_register', __name__,template_folder='../../templates/login-register')



@login_register_bp.route('/', methods=["GET"])
def return_home():
    return render_template('login.html')

@login_register_bp.route('/login-error', methods=["GET"])
def return_home_error():
    return render_template('login.html', error="usuário ou senha inválidos")


@login_register_bp.route('/login', methods=["POST"])
def return_login():
    dados = request.form.to_dict()
    if dados:
        result = Cliente.login(dados)
        if result:
            return render_template('home.html')
        flash("Usuário ou senha inválidos")
        return redirect(url_for("login_register.return_home_error"))
    return jsonify('Dados Inválidos'), 404


@login_register_bp.route('/register', methods=["GET"])
def return_register_page():
    return render_template('register.html')

@login_register_bp.route('/register/user', methods=['POST'])
def register_user():
    dados = request.form.to_dict()
    print(dados)
    if dados:
        result = Cliente.register(dados)
        if result:
            flash('mensagem')
            return redirect(url_for("login_register.return_home"))