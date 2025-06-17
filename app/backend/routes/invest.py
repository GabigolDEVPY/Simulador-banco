from flask import Blueprint, render_template

invest_bp = Blueprint('invest', __name__,template_folder='../../templates/invest')


@invest_bp.route("/invest", methods=["GET"])
def return_invest_page():
    return render_template("invest.html")

@invest_bp.route("/invest/bitcoin", methods=["GET"])
def return_bitcoin_page():
    return render_template("bitcoin.html")

@invest_bp.route("/invest/ethereum", methods=["GET"])
def return_ethereum_page():
    return render_template("ethereum.html")

@invest_bp.route("/invest/dolar", methods=["GET"])
def return_dolar_page():
    return render_template("dolar.html")