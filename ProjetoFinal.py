from time import sleep


poli = "*"*10
nome = ''
telefone = 0
cpf = 0
escolha=False

usuario = {"nome":nome, "telefone":telefone, "cpf":cpf}

while escolha == False:
    escolha2 =False
    escolha3 =False
    cond=False
    s = str(input("\nVocê gostaria de se identificar? \n sim \n nao \n :>"))

    if s == "sim":
        usuario = {"nome":nome, "telefone":telefone, "cpf":cpf}

        print(f"\n {poli} IDENTIFIQUE-SE {poli} \n")

        usuario ["nome"] = str(input("Digite seu nome completo: ")) 

        usuario ["telefone"] = int(input("Digite o número do seu telefone: "))

        usuario ["cpf"] = int(input("Digite o seu CPF: "))

        final = "Obrigado {} pelo contato!! Tenha um otimo dia!".format(usuario['nome'])
        while escolha2==False:
            print("Escolha a opção:\n 1.Reclamção\n2.Alteração de dados\n")
            var=int(input("digite a opção aqui:"))
            if(var==1):
                relato = str(input("Por favor, nos relate o ocorrido: "))
                
                print(final)
                while cond == False:
                    t=str(input("\nGostaria de falar com um de nossos atendentes? \n sim \n nao \n :>"))
                    if  t== "sim":
                        for c in range(10,0,-1):
                            sleep(2)
                            print("Por favor aguarde, estamos direcionando para um de nossos atendentes \n posição na fila: {} de 10".format(c))
                        print("Encaminhado!!")
                        cond=True
                        escolha2=True
                    elif t == "nao": 
                        print(final)
                        cond=True
                        escolha2=True
                        
                    else:
                        cond = False
                        print("Condição inexistente")
            elif var==2:
                print("escolheu 2")
                
                while(escolha3==False):
                    print("Escolha a opção:\n 1.Nome \n2.CPF\n3.Telefone")
                    var=int(input("digite a opção aqui:"))
                    if(var==1):
                        print("escolheu alteração de nome")
                        nome=str(input("Digite o novo nome:"))
                        usuario["nome"]=nome
                        print("seu nome foi alterado para: {}".format(usuario["nome"]))
                        print(final)
                        escolha3=True
                        escolha2=True
                    elif var ==2:
                        print("escolheu alteração de cpf")
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
                            

                            
                            #print(f"Resultado: {validacao1} {validacao2}")
                            
                            if validacao1 and validacao2:
                                print("CPF Válido")
                                escolha2=True
                                escolha3=True
                                usuario["cpf"]=cpf
                                print("seu cpf foi alterado para: {}".format(usuario["cpf"]))
                                print(final)
                            else:
                                print("CPF Inválido")
                                escolha2=True
                                escolha3=True
                                print(final)
                        else:
                            print("CPF inválido")
                            escolha2=True
                            escolha3=True
                            print(final)
                    elif var ==3:
                            print("escolheu alteração de telefone")
                            telefone=str(input("Digite o novo telefone:"))
                            usuario["telefone"]=telefone
                            print("seu telefone foi alterado para: {}".format(usuario["telefone"]))
                            print(final)
                            escolha2=True
                            escolha3=True
                    else:
                            print("valor digitado incorreto \n")
                            
                            escolha3=False
            else:
                print("valor digitado incorreto \n")
                escolha2=False



    elif s == "nao": 
        relato = str(input("Por favor, nos relate o ocorrido: "))
        print("Obrigado por relatar!")

    else:
        
        print("Condição inexistente")
