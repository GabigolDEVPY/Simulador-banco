from flask import Blueprint, render_template
from ..utils.request_api import Get_value
from..utils.auth import login_required

invest_bp = Blueprint('invest', __name__,template_folder='../../templates/invest')


@invest_bp.route("/invest", methods=["GET"])
@login_required
def return_invest_page():
    return render_template("invest.html")


@invest_bp.route("/invest/bitcoin", methods=["GET"])
@login_required
def return_bitcoin_page():
    dados = Get_value.puxar_cripto('https://api.coingecko.com/api/v3/coins/bitcoin')
    return render_template("bitcoin.html", dados=dados)


@invest_bp.route("/invest/ethereum", methods=["GET"])
@login_required
def return_ethereum_page():
    dados = Get_value.puxar_cripto('https://api.coingecko.com/api/v3/coins/ethereum')
    return render_template("ethereum.html", dados=dados)


@invest_bp.route("/invest/dolar", methods=["GET"])
@login_required
def return_dolar_page():
    dados = Get_value.puxar_dolar()
    return render_template("dolar.html", dados=dados)
