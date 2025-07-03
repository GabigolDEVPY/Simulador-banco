from flask import Blueprint, render_template, request, flash, url_for, redirect
from..utils.auth import login_required
from..utils.payment import Payment

transfer_bp = Blueprint('transfer', __name__,template_folder='../../templates/transfer')

@transfer_bp.route('/transfer', methods=['GET'])
@login_required
def return_transfer_page():
    return render_template('transfer.html')

@transfer_bp.route('/conferir-transfer', methods=['POST'])
@login_required
def return_transfer_confer():
    dados = request.form.to_dict()
    result = Payment.pix_sender(dados)
    if result == 1:
        flash('Valor saldo insuficiente, seu pobre!')
        return redirect(url_for("transfer.return_transfer_page"))
    elif result == 2:
        flash('Chave pix inválida')
        return redirect(url_for("transfer.return_transfer_page"))   
    return render_template('transfer-verify.html')

@transfer_bp.route('/result-transfer', methods=['POST'])
@login_required    
def return_result_transfer():
    return render_template('result-transfer.html')