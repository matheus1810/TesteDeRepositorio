# Leia um número inteiro N e exiba a sua tabuada completa (de 1 a 10) no formato 'N x I = resultado'. 

numero = int(input("Digite um número pra saber sua tabuada: "))

contador = 0

while contador <= 10:
    print(f"{numero} X {contador} = {numero*contador}")
    contador+=1