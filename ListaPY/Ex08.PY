#Dicionário – Crie um dicionário com os seguintes campos: 
#• Nome 
#• Idade 
#• Curso 
#Peça os valores ao usuário e ao final exiba o dicionário completo formatado. 

informacoes = { }

informacoes["nome"] = input("Informe o seu nome :")
informacoes["idade"] = int(input("Informe a sua idade :"))
informacoes["curso"] = input("Informe o seu curso :")


for chave, valor in informacoes.items():
    print(f"{chave}:{valor}")
