#Dicionário – Crie um dicionário com 3 produtos e seus preços. Depois permita ao usuário digitar 
#o nome de um produto e mostre seu preço. Se não existir, exiba “Produto não cadastrado”. 

produtos = {
    "pepsi": 5.99,
    "bis": 7.49,
    "doritos": 13.89
}


produto = input("Informe o nome do produto: ").lower()


if produto in produtos:
    print(f"O preço de {produto} é R$ {produtos[produto]:.2f}")
else:
    print("Produto não cadastrado.")
