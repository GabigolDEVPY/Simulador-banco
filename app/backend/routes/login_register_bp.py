from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash, session
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
    if 'login' in session:
        session.clear()
    dados = request.form.to_dict()
    print(dados)
    if dados:
        result = Cliente.login(dados)
        if result:
            result = result[0]
            session['chave_pix'] = result['chave_pix']
            session['login'] = result['user_login']
            print(session['chave_pix'])
            return render_template('home.html', dados=result)
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
            flash('Usuário cadastrado com sucesso!')
            return redirect(url_for("login_register.return_home"))
        flash('Erro ao cadastrar usuário')
        return redirect(url_for("login_register.return_register_page"))
    

@login_register_bp.route("/logout", methods=["GET"])
def logout():
    session.clear()
    flash("Logout realizado com sucesso")
    return redirect(url_for("login_register.return_home"))    