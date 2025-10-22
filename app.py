from flask import Flask, jsonify, request 

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "Ana", "curso": "Computação"},
    {"id": 2, "nome": "Bruno", "curso": "Engenharia de Software"}
]

# Rota GET 
@app.route('/alunos', methods=['GET']) 
def get_alunos():     
    return jsonify(alunos)
# Rota POST 
@app.route('/alunos', methods=['POST']) 
def add_aluno():
    novo = {"id": len(alunos) + 1, **request.json}     
    alunos.append(novo)     
    return jsonify(novo), 201

# Rota PUT 
@app.route('/alunos/<int:id>', methods=['PUT']) 
def update_aluno(id):     
    for aluno in alunos:
        if aluno["id"] == id:             
            aluno.update(request.json)             
            return jsonify(aluno)
    return jsonify({"mensagem": "Aluno não encontrado"}), 404

# Rota DELETE 
@app.route('/alunos/<int:id>', methods=['DELETE']) 
def delete_aluno(id):     
    global alunos     
    alunos = [a for a in alunos if a["id"] != id]     
    return jsonify({"mensagem": "Aluno removido com sucesso"})

if __name__ == '__main__':     
    app.run(debug=True, port=5000)
