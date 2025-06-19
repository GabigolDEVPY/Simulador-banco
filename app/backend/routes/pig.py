from flask import Blueprint, render_template


pig_bp = Blueprint('pig', __name__,template_folder='../../templates/pig')

@pig_bp.route('/pigs', methods=['GET'])
def return_pigs_page():
    caixinhas = [{"nome": "Viagem", "valor": 1300, "imagem": "../static/imgs/viagens.webp"}]
    return render_template('pigs.html', caixinhas=caixinhas, num_caixinhas= 4 - len(caixinhas) )


@pig_bp.route('/pig', methods=['GET'])
def return_pig_page():
    return render_template('pig.html')