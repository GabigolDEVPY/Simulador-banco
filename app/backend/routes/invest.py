from flask import Blueprint, render_template
from ..utils.request_api import Get_value

invest_bp = Blueprint('invest', __name__,template_folder='../../templates/invest')


@invest_bp.route("/invest", methods=["GET"])
def return_invest_page():
    return render_template("invest.html")

@invest_bp.route("/invest/bitcoin", methods=["GET"])
def return_bitcoin_page():
    dados = Get_value.puxar_bitcoin()
    return render_template("bitcoin.html", dados=dados)

@invest_bp.route("/invest/ethereum", methods=["GET"])
def return_ethereum_page():
    dados = Get_value.puxar_ethereum()
    return render_template("ethereum.html", dados=dados)

@invest_bp.route("/invest/dolar", methods=["GET"])
def return_dolar_page():
    return render_template("dolar.html")