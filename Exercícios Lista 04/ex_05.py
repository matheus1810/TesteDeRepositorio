# Defina uma senha no código (ex.: '1234'). 
# Peça ao usuário que a informe. 
# Enquanto a senha estiver errada, exiba 'Senha incorreta. Tente novamente.' Quando acertar, exiba 'Acesso liberado!'. 

senha = 1234

senhaInput = int(input("Digite sua senha: "))

while senhaInput != senha:
    print("Senha Incorreta. Tente novamente")
    senhaInput = int(input("Digite sua senha: "))

print("Acesso Liberado")