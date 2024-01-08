from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from users import Users
from usersrepository import UsersRepository


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/bancosete"
mongo = PyMongo(app)
users_repository = UsersRepository(mongo)

@app.route("/users", methods=["POST"])
def cadastrar_usuario():
    try:
        data = request.get_json()
        users = Users(ObjectId(data['id']), data["nome"], data["email"], data["senha"],"active")
        users.senha = users.criptograr_senha(data["senha"])
        users_repository.criar_usuario(users.nome, users.email, users.senha, users.status)
        return jsonify({'message': 'Usuário cadastrado com sucesso!', 'status':200})
    except:
        return jsonify({'message': 'Erro ao cadastrar usuário!', 'status':500})


@app.route("/users", methods=["GET"])
def listar_usuarios():
    try:
        resp = users_repository.listar_usuarios()
        return jsonify({'usuarios', resp})
    except:
        return jsonify({'message': 'Erro ao listar usuarios!','status':500})


if __name__=='__main__':
    app.run(debug=True)