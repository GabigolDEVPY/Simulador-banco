from flask import Blueprint, render_template, request


pig_bp = Blueprint('pig', __name__,template_folder='../../templates/pig')

imgs_caixinha = ["/static/imgs-caixinha/viagem.jpeg", "/static/imgs-caixinha/carro.jpg", "/static/imgs-caixinha/casa.jpg", "/static/imgs-caixinha/casamento.webp", "/static/imgs-caixinha/cinema.webp", "/static/imgs-caixinha/cofre.jpeg", "/static/imgs-caixinha/moto.jpg", "/static/imgs-caixinha/moveis.jpg", "/static/imgs-caixinha/praia.jpg", "/static/imgs-caixinha/reforma.webp", "/static/imgs-caixinha/reserva.jpeg", "/static/imgs-caixinha/templo.jpg", "/static/imgs-caixinha/videogame.jpg"]

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
        

# CRIAR PORCOOOOOOOOOOOOOOOOOOOOOOOOOOo
@pig_bp.route('/pig/criarpig', methods=["GET", "POST"])

def return_pig_create():
    if request.method == "GET":
      return render_template('criarpig.html', imgs_caixinha=imgs_caixinha)      
    if request.method == "POST":
        dados = request.form.to_dict()
        caixinhas.append(
            {"id": 6, "nome": dados['nome'], "valor": dados['inicial'], "imagem": dados['imagem'], "valor_investido": dados['inicial'], "meta": dados['meta'], "ganhos": 0}
        )
        print(dados)
        return render_template('pigs.html', caixinhas=caixinhas, num_caixinhas= 4 - len(caixinhas))


# GAURDAR VALOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOR
@pig_bp.route('/pigs/pig/guardarpig/<int:id>', methods=["GET"])

def return_guardar_pig(id):
      print(id)
      for caixinha in caixinhas:
        if caixinha['id'] == id:
            return render_template('guardarpig.html', caixinha=caixinha)



@pig_bp.route('/pigs/pig/guardarpig/<int:id>', methods=['POST'])

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
def return_resgatar_valor(id):
        print(id)
        for caixinha in caixinhas:
            if caixinha['id'] == id:
                return render_template('resgatarpig.html', caixinha=caixinha)         
          


@pig_bp.route('/pigs/pig/resgatarpig/<int:id>', methods=['POST'])
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

def delete_pig(id):
    for caixinha in caixinhas:
        if caixinha['id'] == id:
            caixinhas.remove(caixinha)
    return render_template('pigs.html', caixinhas=caixinhas, num_caixinhas= 4 - len(caixinhas))
