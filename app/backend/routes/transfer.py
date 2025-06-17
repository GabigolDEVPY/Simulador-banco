from flask import Blueprint, render_template
import sys
sys.dont_write_bytecode = True

transfer_bp = Blueprint('transfer', __name__,template_folder='../../templates/transfer')

@transfer_bp.route('/transfer', methods=['GET'])
def return_transfer_page():
    return render_template('transfer.html')

@transfer_bp.route('/conferir-transfer', methods=['POST'])
def return_transfer_confer():
    return render_template('transfer-verify.html')

@transfer_bp.route('/result-transfer', methods=['POST'])
def return_result_transfer():
    return render_template('result-transfer.html')