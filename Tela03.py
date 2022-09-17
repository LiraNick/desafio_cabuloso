
escolha =False
while(escolha==False):
    print("Escolha a opção:\n 1.Reclamção\n2.Alteração de dados\n")
    var=int(input("digite a opção aqui:"))
    if(var==1):
        print("escolheu 1")
        escolha=True
    elif var ==2:
        print("escolheu 2")
        escolha=True
    else:
        print("valor digitado incorreto \n")
        escolha=False

