
from flask import Blueprint, render_template, session, abort
from ..utils.cliente import Cliente
from..utils.auth import login_required


home_bp = Blueprint('home', __name__,template_folder='../../templates')


@home_bp.route('/home', methods=["GET"])
def return_home():
    if 'login' in session:
        result = Cliente.login(session['login'])
        return render_template('home.html', dados=result)
    return abort(403)


@home_bp.route('/notify', methods=["GET"])
@login_required
def return_notify():
    dados = Cliente.notify()
    if dados:
        Cliente.zerar_notifys(session["user_id"])
        return render_template('notify.html', dados=dados)
    return render_template('notify.html')


@home_bp.route('/history', methods=["GET"])
@login_required
def return_history():
    dados = Cliente.history()
    if dados:
        return render_template('history.html', dados=dados)
    return render_template('history.html')


