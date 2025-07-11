from flask import Blueprint, render_template, request, flash, url_for, redirect, abort, session
from..utils.auth import login_required
from..utils.payment import Payment
import ast

transfer_bp = Blueprint('transfer', __name__,template_folder='../../templates/transfer')

@transfer_bp.route('/transfer', methods=['GET'])
@login_required
def return_transfer_page():
    return render_template('transfer.html')


@transfer_bp.route('/conferir-transfer', methods=['POST'])
@login_required
def return_transfer_confer():
    dados = request.form.to_dict()
    print("rota 1", dados, session['chave_pix'])
    result = Payment.pix_sender_verify(dados)
    if result == 1:
        flash('Valor saldo insuficiente, seu pobre!')
        return redirect(url_for("transfer.return_transfer_page"))
    elif result == 2:
        flash('Chave pix inválida')
        return redirect(url_for("transfer.return_transfer_page"))   
    elif result == 3:
        flash("Não é possível tranferir pix para sí mesmo")
        return redirect(url_for("transfer.return_transfer_page"))   
        
    else:
        result = result[0]
        return render_template('transfer-verify.html', result=result, valor=float(dados['valor']))


@transfer_bp.route('/result-transfer/<valor>', methods=['GET'])
@login_required    
def result_transfer_page_get(valor):
    dados_result = session.pop('dados', None)
    if not dados_result:
        flash("Dados não encontrados.")
        return redirect(url_for('transfer.return_transfer_page'))
    return render_template("result-transfer.html", dados=dados_result, valor=valor)


@transfer_bp.route('/result-transfer/<result>/<valor>', methods=['POST'])
@login_required    
def return_result_transfer(result, valor):
    dados = ast.literal_eval(result)
    senha = request.form.to_dict()
    dados['valor'] = float(valor)
    dados['validado'] = "validado"
    dados['user_password'] = senha['user_password']
    result = Payment.pix_sender_verify(dados)
    if result == 4:
        flash("Senha incorreta")
        return redirect(url_for("transfer.return_transfer_page"))
    session['dados'] = dados_result = Payment.dados_result(dados)
    print(session['dados'])  
    return redirect(url_for('transfer.result_transfer_page_get', valor=valor))