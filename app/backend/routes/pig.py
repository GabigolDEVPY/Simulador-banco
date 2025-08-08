from flask import Blueprint, render_template, request, url_for, redirect, flash
from..utils.auth import login_required
from ..utils.pig import Pig
from ..utils.cliente import Cliente

pig_bp = Blueprint('pig', __name__,template_folder='../../templates/pig')

imgs_caixinha = ["/static/imgs-caixinha/viagem.jpeg", "/static/imgs-caixinha/carro.jpg", "/static/imgs-caixinha/casa.jpg", "/static/imgs-caixinha/casamento.webp", "/static/imgs-caixinha/cinema.webp", "/static/imgs-caixinha/cofre.jpeg", "/static/imgs-caixinha/moto.jpg", "/static/imgs-caixinha/moveis.jpg", "/static/imgs-caixinha/praia.jpg", "/static/imgs-caixinha/reforma.webp", "/static/imgs-caixinha/reserva.jpeg", "/static/imgs-caixinha/templo.jpg", "/static/imgs-caixinha/videogame.jpg"]


@pig_bp.route('/pigs', methods=['GET'])
@login_required
def return_pigs_page():
    caixinhas, num_caixinhas = Pig.return_pigs()
    return render_template('pigs.html', caixinhas=caixinhas, num_caixinhas= 4 - num_caixinhas, total_bruto=Pig.return_bruto())


@pig_bp.route('/pigs/pig/<int:id>', methods=['GET'])
@login_required
def return_pig_page(id):
    return render_template('pig.html', caixinha=Pig.return_pig(id))
        

@pig_bp.route('/pig/criarpig', methods=["GET", "POST"])
@login_required
def return_pig_create():
    if request.method == "GET":
        return render_template('criarpig.html', imgs_caixinha=imgs_caixinha)      
    if request.method == "POST":
        Pig.criar_pig(request.form.to_dict())
        return redirect((url_for("pig.return_pigs_page")))


@pig_bp.route('/pigs/pig/guardarpig/<int:id>', methods=["GET"])
@login_required
def return_guardar_pig(id):
    return render_template('guardarpig.html', caixinha=Pig.return_pig(id), value=Cliente.value_user())


@pig_bp.route('/pigs/pig/guardarpig/<int:id>', methods=['POST'])
@login_required
def guardar_valor(id):
        result = Pig.guardar_pig(request.form.to_dict(), id)
        if result == 0:
            flash("Valor insuficiente na conta!")
            return redirect(url_for('pig.return_guardar_pig', id=id))
        elif result == 2:
            flash("Senha incorreta")
            return redirect(url_for('pig.return_guardar_pig', id=id))
        
        return redirect(url_for('pig.return_pig_page', id=id))


# RESGATAR VALORRRRRRRRRRRRRRRRRRRRRRRRRRR
@pig_bp.route('/pigs/pig/resgatarpig/<int:id>', methods=['GET'])
@login_required
def return_resgatar_valor(id):
    print("iddd", id)
    caixinha = Pig.return_pig(id)
    print(caixinha)
    return render_template('resgatarpig.html', caixinha=caixinha)         


@pig_bp.route('/pigs/pig/resgatarpig/<int:id>', methods=['POST'])
@login_required
def resgatar_valor(id):
    if request.method == 'POST':
        dados = request.form.to_dict()
        print(dados, "id", id)
        caixinhas = Pig.return_pigs()
        for caixinha in caixinhas:
            if caixinha['pig_id'] == id:
                caixinha['valor'] = (caixinha['valor'] - int(dados['value']))
                return render_template('pig.html', caixinha=caixinha)    


# DELETAR CAIXINHAAAA
@pig_bp.route('/pigs/pig/deletepig/<int:id>', methods=["GET"])
@login_required
def delete_pig(id):
    Pig.deletar_pig(id)
    return redirect(url_for("pig.return_pigs_page"))

