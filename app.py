from flask import Flask, jsonify, request

app = Flask(__name__)

dietas = [
    {"id": 1, "nome": "Dieta Cetogênica", "descricao": "Alta em gorduras e baixa em carboidratos", "calorias": 1500},
    {"id": 2, "nome": "Dieta Mediterrânea", "descricao": "Baseada em alimentos naturais como azeite e peixe", "calorias": 1800},
    {"id": 3, "nome": "Dieta Paleolítica", "descricao": "Foca em alimentos não processados", "calorias": 1600},
    {"id": 4, "nome": "Dieta Vegana", "descricao": "Livre de produtos de origem animal", "calorias": 1700},
    {"id": 5, "nome": "Dieta Vegetariana", "descricao": "Sem carne, mas com ovos e laticínios", "calorias": 1800},
    {"id": 6, "nome": "Dieta Atkins", "descricao": "Baixo carboidrato, alta proteína", "calorias": 2000},
    {"id": 7, "nome": "Dieta DASH", "descricao": "Para controle da hipertensão", "calorias": 1900},
    {"id": 8, "nome": "Dieta Detox", "descricao": "Foca em desintoxicação", "calorias": 1200},
    {"id": 9, "nome": "Dieta Flexitariana", "descricao": "Principalmente vegetariana, com carne ocasionalmente", "calorias": 1700},
    {"id": 10, "nome": "Dieta Nórdica", "descricao": "Baseada em peixes, raízes e vegetais", "calorias": 1800},
    {"id": 11, "nome": "Dieta Low Carb", "descricao": "Baixa em carboidratos", "calorias": 1400},
    {"id": 12, "nome": "Dieta Alcalina", "descricao": "Equilibra pH do corpo", "calorias": 1500},
    {"id": 13, "nome": "Dieta do Jejum Intermitente", "descricao": "Jejum por períodos prolongados", "calorias": 2000},
    {"id": 14, "nome": "Dieta Cetogênica Cíclica", "descricao": "Ciclos de carboidrato e gordura", "calorias": 1600},
    {"id": 15, "nome": "Dieta Whole30", "descricao": "Elimina alimentos processados", "calorias": 1400},
    {"id": 16, "nome": "Dieta da Zona", "descricao": "Equilíbrio entre proteínas, carboidratos e gorduras", "calorias": 1700},
    {"id": 17, "nome": "Dieta Sem Glúten", "descricao": "Livre de glúten", "calorias": 1500},
    {"id": 18, "nome": "Dieta Low FODMAP", "descricao": "Reduz alimentos fermentáveis", "calorias": 1600},
    {"id": 19, "nome": "Dieta Carnívora", "descricao": "Baseada em carne e produtos animais", "calorias": 2200},
    {"id": 20, "nome": "Dieta Frugívora", "descricao": "Baseada em frutas", "calorias": 1300},
    {"id": 21, "nome": "Dieta Macrobiótica", "descricao": "Baseada em cereais integrais e vegetais", "calorias": 1500},
    {"id": 22, "nome": "Dieta Hiperproteica", "descricao": "Alta ingestão de proteínas", "calorias": 2100},
    {"id": 23, "nome": "Dieta Anti-inflamatória", "descricao": "Reduz inflamações", "calorias": 1800},
    {"id": 24, "nome": "Dieta Volumétrica", "descricao": "Foca em alimentos de baixa densidade calórica", "calorias": 1600},
    {"id": 25, "nome": "Dieta HCG", "descricao": "Baseada no uso do hormônio HCG", "calorias": 1000}
]

@app.route('/dietas', methods=['GET'])
def get_dietas():
    return jsonify(dietas)

@app.route('/dietas/<int:id>', methods=['GET'])
def get_dieta(id):
    dieta = next((dieta for dieta in dietas if dieta["id"] == id), None)
    if dieta is None:
        return jsonify({"message": "Dieta não encontrada"}), 404
    return jsonify(dieta)

@app.route('/dietas', methods=['POST'])
def add_dieta():
    nova_dieta = request.get_json()
    nova_dieta["id"] = len(dietas) + 1
    dietas.append(nova_dieta)
    return jsonify(nova_dieta), 201

@app.route('/dietas/<int:id>', methods=['PUT'])
def update_dieta(id):
    dieta = next((dieta for dieta in dietas if dieta["id"] == id), None)
    if dieta is None:
        return jsonify({"message": "Dieta não encontrada"}), 404
    dados_atualizados = request.get_json()
    dieta.update(dados_atualizados)
    return jsonify(dieta)

@app.route('/dietas/<int:id>', methods=['DELETE'])
def delete_dieta(id):
    global dietas
    dietas = [dieta for dieta in dietas if dieta["id"] != id]
    return jsonify({"message": "Dieta deletada"}), 200

if __name__ == '__main__':
    app.run(debug=True)