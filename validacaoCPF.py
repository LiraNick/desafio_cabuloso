cpf = str(input("Digite um CPF válido (somente números):"))

#Verifica se o CPF digitado possui apenas 11 dígitos
if len(cpf) == 11:
    #entra nas outras validações
    validacao1 = False    
    
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
        print("CPF Válido")
    else:
        print("CPF Inválido")
else:
    print("CPF inválido")

