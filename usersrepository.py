

class UsersRepository:
    def __init__(self, mongo): 
         self.mongo = mongo
         
    def obter_usuario_id(self, id):
        return self.mongo.db.users.find_one({"_id":ObjectId(self.id)})

    def obter_usuario_email(self,email):
        return self.mongo.db.users.find_one({"email": self.email})
    
    def listar_usuarios(self):
        return self.mongo.db.users.find()
    
    def criar_usuario(self, nome, email, senha, status):
        return self.mongo.db.users.insert_one({
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "status": self.status
        })