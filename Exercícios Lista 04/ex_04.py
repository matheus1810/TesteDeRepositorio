# Gere (ou fixe no código) um número secreto entre 1 e 100. 
# O usuário tenta adivinhar: se o chute for menor, exiba 'Muito baixo!'; se for maior, 'Muito alto!'; se acertar, exiba 'Parabéns! 
# Você acertou em X tentativas.' e encerre. 


numeroSecreto = 10
numeroDeTentativas = 0



while True:
    numeroInput = int(input("Digite um numero para ser sorteado: "))
    numeroDeTentativas +=1
    if numeroInput < numeroSecreto:
        print("Muito baixo! ")
    elif numeroInput > numeroSecreto:
        print("Muito alto! ")
    else:
        print(f"Parabéns, você acertou em {numeroDeTentativas} tentativas")
        break
    
    


    