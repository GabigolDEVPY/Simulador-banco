from flask import Blueprint, render_template

transfer_bp = Blueprint('transfer', __name__,template_folder='../../templates/transfer')

@transfer_bp.route('/transfer', methods=['GET'])
def return_transfer_page():
    return render_template('transfer.html')