class Usuario:
    def __init__(self, nome, telefone, cpf):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf

    def mostraDados(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'CPF: {self.cpf}')
        
    
