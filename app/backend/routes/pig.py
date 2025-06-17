from flask import Blueprint, render_template


pig_bp = Blueprint('pig', __name__,template_folder='../../templates/pig')

@pig_bp.route('/pigs', methods=['GET'])
def return_pigs_page():
    return render_template('pigs.html')


@pig_bp.route('/pig', methods=['GET'])
def return_pig_page():
    return render_template('pig.html')