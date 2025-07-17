from flask import Blueprint, render_template, request
from..utils.auth import login_required
from ..utils.pig import Pig

pig_bp = Blueprint('pig', __name__,template_folder='../../templates/pig')

imgs_caixinha = ["/static/imgs-caixinha/viagem.jpeg", "/static/imgs-caixinha/carro.jpg", "/static/imgs-caixinha/casa.jpg", "/static/imgs-caixinha/casamento.webp", "/static/imgs-caixinha/cinema.webp", "/static/imgs-caixinha/cofre.jpeg", "/static/imgs-caixinha/moto.jpg", "/static/imgs-caixinha/moveis.jpg", "/static/imgs-caixinha/praia.jpg", "/static/imgs-caixinha/reforma.webp", "/static/imgs-caixinha/reserva.jpeg", "/static/imgs-caixinha/templo.jpg", "/static/imgs-caixinha/videogame.jpg"]


@pig_bp.route('/pigs', methods=['GET'])
@login_required
def return_pigs_page():
    caixinhas = Pig.return_pigs()
    return render_template('pigs.html', caixinhas=caixinhas, num_caixinhas= 4 - len(caixinhas) )




@pig_bp.route('/pigs/pig/<int:id>', methods=['GET'])
@login_required
def return_pig_page(id):
    caixinhas = Pig.return_pigs()
    for caixa in caixinhas:
        if caixa['pig_id'] == id:
            return render_template('pig.html', caixinha=caixa)
        

# CRIAR PORCOOOOOOOOOOOOOOOOOOOOOOOOOOo
@pig_bp.route('/pig/criarpig', methods=["GET", "POST"])
@login_required
def return_pig_create():
    if request.method == "GET":
        return render_template('criarpig.html', imgs_caixinha=imgs_caixinha)      
    if request.method == "POST":
        dados = request.form.to_dict()
        Pig.criar_pig(dados)
        print(dados)
        caixinhas = Pig.return_pigs()
        return render_template('pigs.html', caixinhas=caixinhas, num_caixinhas= 4 - len(caixinhas))


# GAURDAR VALOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOR
@pig_bp.route('/pigs/pig/guardarpig/<int:id>', methods=["GET"])
@login_required
def return_guardar_pig(id):
      print(id)
      for caixinha in caixinhas:
        if caixinha['id'] == id:
            return render_template('guardarpig.html', caixinha=caixinha)



@pig_bp.route('/pigs/pig/guardarpig/<int:id>', methods=['POST'])
@login_required
def guardar_valor(id):
    if request.method == 'POST':
        dados = request.form.to_dict()
        print(dados, "id", id)
        for caixinha in caixinhas:
            if caixinha['id'] == id:
                caixinha['valor'] = (caixinha['valor'] + int(dados['value']))
                return render_template('pig.html', caixinha=caixinha)    


# RESGATAR VALORRRRRRRRRRRRRRRRRRRRRRRRRRR
@pig_bp.route('/pigs/pig/resgatarpig/<int:id>', methods=['GET'])
@login_required
def return_resgatar_valor(id):
        print(id)
        for caixinha in caixinhas:
            if caixinha['id'] == id:
                return render_template('resgatarpig.html', caixinha=caixinha)         



@pig_bp.route('/pigs/pig/resgatarpig/<int:id>', methods=['POST'])
@login_required
def resgatar_valor(id):
    if request.method == 'POST':
        dados = request.form.to_dict()
        print(dados, "id", id)
        for caixinha in caixinhas:
            if caixinha['id'] == id:
                caixinha['valor'] = (caixinha['valor'] - int(dados['value']))
                return render_template('pig.html', caixinha=caixinha)    


# DELETAR CAIXINHAAAA
@pig_bp.route('/pigs/pig/deletepig/<int:id>', methods=["GET"])
@login_required
def delete_pig(id):
    for caixinha in caixinhas:
        if caixinha['id'] == id:
            caixinhas.remove(caixinha)
    return render_template('pigs.html', caixinhas=caixinhas, num_caixinhas= 4 - len(caixinhas))
