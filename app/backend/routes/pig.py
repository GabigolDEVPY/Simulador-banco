from flask import Blueprint, render_template, request


pig_bp = Blueprint('pig', __name__,template_folder='../../templates/pig')

caixinhas = [
        {"id": 1, "nome": "Viagem", "valor": 1300, "imagem": "/static/imgs-caixinha/viagem.jpeg", "valor_investido": 1200, "meta": 20000, "ganhos": 254},        
        {"id": 5, "nome": "Avião", "valor": 10000, "imagem": "/static/imgs-caixinha/carro.jpg", "valor_investido": 3000, "meta": 23644, "ganhos": 212},        
        {"id": 9, "nome": "Carro", "valor": 2500, "imagem": "/static/imgs-caixinha/videogame.jpg", "valor_investido": 5000, "meta": 50078, "ganhos": 234}             
]

@pig_bp.route('/pigs', methods=['GET'])
def return_pigs_page():
    return render_template('pigs.html', caixinhas=caixinhas, num_caixinhas= 4 - len(caixinhas) )


@pig_bp.route('/pigs/pig/<int:id>', methods=['GET'])
def return_pig_page(id):
    for caixa in caixinhas:
        if caixa['id'] == id:
            return render_template('pig.html', caixinha=caixa)
        
@pig_bp.route('/pig/criarpig', methods=["GET"])
def return_pig_create():
    return render_template('criarpig.html')      

@pig_bp.route('/pigs/pig/guardarpig/<int:id>', methods=["GET"])
def return_guardar_pig(id):
      print(id)
      for caixinha in caixinhas:
        if caixinha['id'] == id:
            return render_template('guardarpig.html', caixinha=caixinha)          

@pig_bp.route('/pigs/pig/deletepig/<int:id>', methods=["GET"])
def delete_pig(id):
    for caixinha in caixinhas:
        if caixinha['id'] == id:
            caixinhas.remove(caixinha)