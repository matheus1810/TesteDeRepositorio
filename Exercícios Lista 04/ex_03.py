# Leia números inteiros do usuário repetidamente. 
# Encerre quando o usuário digitar 0. 
# Ao final, Exiba a soma de todos os números digitados (excluindo o zero). 

numero = int(input("Digite um número inteiro: "))

soma = 0


while numero != 0:
    soma+=numero
    numero = int(input("Digite um número inteiro: "))

print(f"A soma é: {soma}")
    
