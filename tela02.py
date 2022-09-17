
poli = "*"*10
nome = ''
telefone = 0
cpf = 0

usuario = {"nome":nome, "telefone":telefone, "cpf":cpf}

print(f"\n {poli} IDENTIFIQUE-SE {poli} \n")

usuario ["nome"] = str(input("Digite seu nome completo: ")) 

usuario ["telefone"] = int(input("Digite o número do seu telefone: "))

usuario ["cpf"] = int(input("Digite o seu CPF: "))

print(usuario)

print ("\nObrigado, {}!" .format(usuario ["nome"]))
