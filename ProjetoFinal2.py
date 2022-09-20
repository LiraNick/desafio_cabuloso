from importlib.metadata import requires
from time import sleep
import os
from Usuario import Usuario



def validaCPF(cpf):
    if len(cpf) == 11:
        #Primeira validação
        #Multiplica-se os 9 primeiros dígitos pela sequência decrescente de números de 10 à 2 e soma os resultados.
        resultado = 0
        c = 10
        for i in range(9):
            resultado = resultado+(int(cpf[i])*c)
            c = c-1
        
        #Multiplicarmos esse resultado por 10 e dividirmos por 11
        resultado = (resultado*10)%11
        
        #Se o resto da divisão for igual a 10, nós o consideramos como 0
        if resultado == 10:
            resultado = 0
        
        #O resultado que nos interessa na verdade é o RESTO da divisão.
        #Se ele for igual ao primeiro dígito verificador (primeiro dígito depois do '-'),
        #a primeira parte da validação está correta.
        
        if resultado == int(cpf[9]):
            validacao1 = True

        #Segunda validação
        
        #A validação do segundo dígito é semelhante à primeira,
        #porém vamos considerar os 9 primeiros dígitos,
        #mais o primeiro dígito verificador,
        #e vamos multiplicar esses 10 números pela sequencia decrescente de 11 a 2.
        
        validacao2 = False
        resultado = 0
        c = 11
        for i in range(10):
            resultado = resultado+(int(cpf[i])*c)
            c = c-1

        #Seguindo o mesmo processo da primeira verificação, multiplicamos por 10 e dividimos por 11
        #Verificando o RESTO, como fizemos anteriormente    
        resultado = (resultado*10)%11
        
        #Verificamos, se o resto corresponde ao segundo dígito verificador.
        if resultado == int(cpf[10]):
            validacao2 = True
        
        #Verificamos se as duas ações são verdadeiras e retornamos como CPF válido
        if validacao1 and validacao2:
            return True
        else:
            return False

    else:
        return False      


nome = ''
telefone = 0
cpf = 0
loopExit=False

pessoa = []

os.system('cls' if os.name == 'nt' else 'clear')

usuario = {"nome":nome, "telefone":telefone, "cpf":cpf}

usuario ["nome"] = str(input("Digite seu nome completo: ")) 
usuario ["telefone"] = int(input("Digite o número do seu telefone: "))
usuario ["cpf"] = int(input("Digite o seu CPF: "))

pessoa.append(Usuario(usuario["nome"], usuario["telefone"], usuario["cpf"]))
pessoa.append(Usuario("Jean", 48484,84848))


for i in range(0, len(pessoa)):
    pessoa[i].mostraDados()

exitCondition = False

#Início do looping do programa
os.system('cls' if os.name == 'nt' else 'clear')

while exitCondition == False:
    print("Bem vindo ao sistema de cadastro de pessoas e reclamações!")
    print("Escolha uma opção:")
    print("1 - Cadastrar usuários")
    print("2 - Listar usuários")
    print("3 - Registrar um problema")
    print("5 - Sair")
    menuSelect = int(input(' ::'))
    
    if menuSelect == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Entre com os dados do usuário:")
        usuario ["nome"] = str(input("Digite seu nome completo: ")) 
        usuario ["telefone"] = int(input("Digite o número do seu telefone: "))
        
        #Validação de CPF, se for verdadeiro, cadastra se não pula/cancela cadastro.
        validaCpfCondicao = False
        while validaCpfCondicao == False:
            usuario ["cpf"] = str(input("Digite o seu CPF: "))
            if validaCPF(usuario["cpf"]):
                validaCpfCondicao = True
                pessoa.append(Usuario(usuario["nome"], usuario["telefone"], usuario["cpf"]))
                #Mostra pessoa cadastrada
                print(f"Usuário {pessoa[len(pessoa)-1].nome} com CPF:{pessoa[len(pessoa)-1].cpf} cadastrado com sucesso!")
                print("")
            else:
                print("CPF Inválido! Gostaria de prosseguir?")
                print("1 - Ajustar")
                print("2 - Cancelar")
                condicaoContinua = int(input("::"))
                if condicaoContinua == 1:
                    validaCpfCondicao = False
                else:
                    validaCpfCondicao = True
                    
                    
    elif menuSelect == 2:
        pass
    
    elif menuSelect == 3:
        pass    
    elif menuSelect == 5:
        exitCondition = True;
        print("Tchau!")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção inválida!\n\n")