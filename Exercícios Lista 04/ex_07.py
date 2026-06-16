# Leia um número inteiro positivo N. 
# Faça uma contagem regressiva de N até 1, exibindo cada número. 
# Ao chegar em 0, exiba 'FOGO!'. Se N for menor ou igual a 0, exiba 'Valor inválido!'. 


numero = int(input("Digite um número inteiro: "))

contador = 0 

while numero > contador:
    numero -=1
    print(numero)
    
print("Fogo")