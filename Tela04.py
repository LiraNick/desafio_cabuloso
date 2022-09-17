
escolha =False
while(escolha==False):
    print("Escolha a opção:\n 1.Nome \n2.CPF\n3.Telefone")
    var=int(input("digite a opção aqui:"))
    if(var==1):
        print("escolheu 1")
        escolha=True
    elif var ==2:
        print("escolheu 2")
        escolha=True
    elif var ==3:
        print("escolheu 3")
        escolha=True    
    else:
        print("valor digitado incorreto \n")
        escolha=False