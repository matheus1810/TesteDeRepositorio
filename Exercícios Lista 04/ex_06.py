# Leia um número inteiro não-negativo N e calcule seu fatorial usando um laço while. 
# Exiba o resultado no formato 'N! = resultado'. Trate o caso N = 0 (0! = 1). 

numero = int(input("Digite um número Inteiro: "))


fatorial = 1

while numero > 0:
    print(numero)
    fatorial = numero*fatorial
    numero -=1
    


print(f"Fatorial:{fatorial}")


