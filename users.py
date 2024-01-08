class Users:
    def __init__(self,  nome, email,senha,status):
        self.nome=nome 
        self.email=email
        self.senha=senha
        self.status=status

    def __str__(self):
        return f" nome={self.nome}, email={self.email}, status={self.status}"
