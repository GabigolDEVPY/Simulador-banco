from flask import Blueprint, render_template, request, url_for, redirect, flash
from ..utils.request_api import Get_value
from..utils.auth import login_required
from..utils.invest import Create_class
from..utils.cliente import Cliente

invest_bp = Blueprint('invest', __name__,template_folder='../../templates/invest')


@invest_bp.route("/invest", methods=["GET"])
@login_required
def return_invest_page():

    criptos = Create_class()
    return render_template("invest.html", criptos=criptos.__dict__, bruto=Cliente().value_user())


@invest_bp.route("/invest/bitcoin", methods=["GET"])
@login_required
def return_bitcoin_page():
    dados = Get_value.puxar_cripto('https://api.coingecko.com/api/v3/coins/bitcoin')
    criptos = (Create_class()).__dict__
    criptos['bruto'] = float(criptos["bitcoin"]) * float(dados["preco"])
    return render_template("bitcoin.html", dados=dados, criptos=criptos)


@invest_bp.route("/invest/ethereum", methods=["GET"])
@login_required
def return_ethereum_page():
    dados = Get_value.puxar_cripto('https://api.coingecko.com/api/v3/coins/ethereum')
    criptos = (Create_class()).__dict__
    criptos['bruto'] = float(criptos["ethereum"]) * float(dados["preco"])
    return render_template("ethereum.html", dados=dados, criptos=criptos)


@invest_bp.route("/invest/dolar", methods=["GET"])
@login_required
def return_dolar_page():
    dados = Get_value.puxar_dolar()
    criptos = (Create_class()).__dict__
    criptos['bruto'] = float(criptos["dolar"]) * float(dados["preco"])
    return render_template("dolar.html", dados=dados, criptos=criptos)

@invest_bp.route("/comprar", methods=["POST"])
def comprar():
    data = request.form.to_dict()
    Criptos = Create_class()
    result =  Criptos.add_cripto(data)
    if result == 1:
        flash("Valor insuficiente na carteira")
        return redirect(url_for("invest.return_invest_page"))
    return redirect(url_for("invest.return_invest_page"))

@invest_bp.route("/vender", methods=["POST"])
def vender():
    data = request.form.to_dict()
    print(data)
    Criptos = Create_class()
    result =  Criptos.remove_cripto(data)
    if result == 1:
        flash("Valor insuficiente na carteira de criptos")
        return redirect(url_for("invest.return_invest_page"))
    return redirect(url_for("invest.return_invest_page"))