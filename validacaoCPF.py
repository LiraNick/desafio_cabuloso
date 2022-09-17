

cpf = str(input("Digite um CPF válido (somente números):"))
#52998224725

if len(cpf) == 11:
    #entra nas outras validações
    validacao1 = False    
    #Primeira validação
    resultado = 0
    c = 10
    for i in range(9):
        resultado = resultado+(int(cpf[i])*c)
        print(f"index da string:{i}: soma: {cpf[i]} * {c} ")
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
        print(f"index da string:{i}: soma: {cpf[i]} * {c} ")
        c = c-1
    
    #print(f"Total das multiplicações segunda parte:{resultado}")
    
    resultado = (resultado*10)%11
    
    #print(f"Resto da divisão: {resultado} tem que ser igual a {cpf[10]}")
    
    if resultado == int(cpf[10]):
        validacao2 = True
    

    
    #print(f"Resultado: {validacao1} {validacao2}")
    
    if validacao1 and validacao2:
        print("CPF Válido")
    else:
        print("CPF Inválido")
else:
    print("CPF inválido")

