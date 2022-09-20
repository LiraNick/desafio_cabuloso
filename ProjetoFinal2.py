from time import sleep
import os

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

        #=============
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


poli = "*"*10
nome = ''
telefone = 0
cpf = 0
escolha=False

usuario = {"nome":nome, "telefone":telefone, "cpf":cpf}
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

while escolha == False:
    escolha2 =False
    escolha3 =False
    cond=False
    s = str(input("\nVocê gostaria de se identificar? \n 1.sim \n 2.nao \n :>"))

    if s == "sim" or 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        usuario = {"nome":nome, "telefone":telefone, "cpf":cpf}

        print(f"\n {poli} IDENTIFIQUE-SE {poli} \n")

        usuario ["nome"] = str(input("Digite seu nome completo: ")) 
        usuario ["telefone"] = int(input("Digite o número do seu telefone: "))
        usuario ["cpf"] = int(input("Digite o seu CPF: "))

        # Não sei o que isso significa 
        # final = "Obrigado {} pelo contato!! Tenha um otimo dia!".format(usuario['nome'])
        
        
        while escolha2==False:
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Escolha a opção:\n1.Reclamção\n2.Alteração de dados\n")
            
            var=int(input("digite a opção aqui:"))
            if(var==1):
                
                os.system('cls' if os.name == 'nt' else 'clear')
                relato = str(input("Por favor, nos relate o ocorrido: "))
                
            #Nao mostrar isso
            # print(final)
                while cond == False:
                    t=str(input("\nGostaria de falar com um de nossos atendentes? \n1.sim \n2.nao \n :>"))
                    if  t== "sim" or t==1:
                        
                        os.system('cls' if os.name == 'nt' else 'clear')
                        for c in range(10,0,-1):
                            sleep(1)
                            print("Por favor aguarde, estamos direcionando para um de nossos atendentes \n posição na fila: {} de 10".format(c))
                        print("Encaminhado!!")
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        cond=True
                        escolha2=True
                    elif t == "nao" or t==2: 
                        #print(final)
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        cond=True
                        escolha2=True
                        
                    else:
                        cond = False
                        print("Condição inexistente")
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
            elif var==2:
                print("escolheu 2")
                os.system('cls' if os.name == 'nt' else 'clear')
                while(escolha3==False):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Escolha a opção:\n1.Nome \n2.CPF\n3.Telefone")
                    var=int(input("digite a opção aqui:"))
                    if(var==1):
                        print("escolheu alteração de nome")
                        nome=str(input("Digite o novo nome:"))
                        usuario["nome"]=nome
                        print("seu nome foi alterado para: {}".format(usuario["nome"]))
                        print("obrigado {} pelo contato!".format(usuario["nome"]))
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        escolha3=True
                        escolha2=True
                    elif var ==2:
                        print("escolheu alteração de cpf")
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        
                        validacaoMaster = False
                        
                        #Loop de validação de CPF enquanto não for válido fica pedindo.
                        while validacaoMaster == False:
                        
                            cpf = str(input("Digite um CPF válido (somente números):"))
                            if len(cpf) == 11:
                                #entra nas outras validações
                                validacao1 = False    
                                #Primeira validação
                                resultado = 0
                                c = 10
                                for i in range(9):
                                    resultado = resultado+(int(cpf[i])*c)
                                    
                                    c = c-1
                                #print(f"Total das multiplicações primera parte:{resultado}")
                                
                                resultado = (resultado*10)%11
                                if resultado == 10:
                                    resultado = 0
                                
                                #print(f"Resto da divisão: {resultado} tem que ser igual a {cpf[9]}")
                                
                                if resultado == int(cpf[9]):
                                    validacao1 = True
                                    
                                #print(f"Resto da divisão: {(resultado*10)%11}")
                                
                                #print("Primeira Validação correta")
                                #=============
                                #Segunda validação
                                validacao2 = False
                                resultado = 0
                                c = 11
                                for i in range(10):
                                    resultado = resultado+(int(cpf[i])*c)
                                    
                                    c = c-1
                                
                                #print(f"Total das multiplicações segunda parte:{resultado}")
                                
                                resultado = (resultado*10)%11
                                
                                #print(f"Resto da divisão: {resultado} tem que ser igual a {cpf[10]}")
                                
                                if resultado == int(cpf[10]):
                                    validacao2 = True
                                
                                if validacao1 and validacao2:
                                    validacaoMaster = True
                                
                                #print(f"Resultado: {validacao1} {validacao2}")
                                
                                if validacao1 and validacao2:
                                    print("CPF Válido")
                                    escolha2=True
                                    escolha3=True
                                    usuario["cpf"]=cpf
                                    print("seu cpf foi alterado para: {}".format(usuario["cpf"]))
                                    print(final)
                                    sleep(2)
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                else:
                                    print("CPF Inválido")
                                    escolha2=True
                                    escolha3=True
                                    print(final)
                                    sleep(2)
                                    os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print("CPF inválido")
                                escolha2=True
                                escolha3=True
                                print(final)
                                sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                
                            #fim do while de teste de CPF
                            
                    elif var ==3:
                            
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("escolheu alteração de telefone")
                            telefone=str(input("Digite o novo telefone:"))
                            usuario["telefone"]=telefone
                            print("seu telefone foi alterado para: {}".format(usuario["telefone"]))
                            print(final)
                            sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            escolha2=True
                            escolha3=True
                    else:
                            print("valor digitado incorreto \n")
                            sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            escolha3=False
            else:
                print("valor digitado incorreto \n")
                sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                escolha2=False



    elif s == "nao" or 2: 
        
        relato = str(input("Por favor, nos relate o ocorrido: "))
        print("Obrigado por relatar!")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        
        print("Condição inexistente")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
