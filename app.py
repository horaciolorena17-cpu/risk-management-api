from flask import Flask, request, jsonify

app = Flask(__name__)

riscos = []

def classificar_risco(probabilidade, impacto):
    score = probabilidade * impacto
    if score >= 15:
        return "Alto"
    elif score >= 6:
        return "Médio"
    else:
        return "Baixo"

@app.route('/risco', methods=['POST'])
def criar_risco():
    data = request.json
    
    probabilidade = data.get("probabilidade", 1)
    impacto = data.get("impacto", 1)
    
    nivel = classificar_risco(probabilidade, impacto)
    
    risco = {
        "id": len(riscos),
        "descricao": data.get("descricao"),
        "probabilidade": probabilidade,
        "impacto": impacto,
        "nivel": nivel
    }
    
    riscos.append(risco)
    
    return jsonify(risco), 201

@app.route('/riscos', methods=['GET'])
def listar_riscos():
    return jsonify(riscos)

if __name__ == '__main__':
    app.run(debug=True)
