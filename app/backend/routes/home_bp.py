
from flask import Blueprint, render_template, session
from ..utils.cliente import Cliente


home_bp = Blueprint('home', __name__,template_folder='../../templates')


@home_bp.route('/home', methods=["GET"])
def return_home():
    if 'login' and 'senha' in session:
        dados = {'login': session['login'], 'senha': session['senha']}
        result = (Cliente.login(dados))[0]
        return render_template('home.html', dados=result)
    return "error"

@home_bp.route('/notify', methods=["GET"])
def return_notify():
    return render_template('notify.html')


@home_bp.route('/history', methods=["GET"])

def return_history():
    return render_template('history.html')


