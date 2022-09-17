# “Obrigada por relatar. Gostaria de falar com um de nossos atentes?” Caixa de seleção: “Sim” ou “Não”




cond = False
print("Obrigado por relatar!")
while cond == False:
     
    cond = str(input("\nGostaria de falar com um de nossos atendentes? \n sim \n nao \n :>"))
        
    if cond == "sim":
        print("Você está sendo transferido para um de nossos atendentes")
        cond = True
        
    elif cond == "nao": 
        print("Obrigado.")
        cond = True 
        
    else:
        cond = False
        print("Condição inexistente")
        
