#TELA 01 - Nicolas
#Pesquisa de Satisfação
#“Você gostaria de se identificar?”
#Caixa de seleção: “Sim” ou “Não”
cond=False
while cond == False:

    cond = str(input("\nVocê gostaria de se identificar? \n sim \n nao \n :>"))

    if cond == "sim":
        print("certo")
        cond = True

    elif cond == "nao": 
        print("Obrigado.")
        cond = True

    else:
        cond = False
        print("Condição inexistente")