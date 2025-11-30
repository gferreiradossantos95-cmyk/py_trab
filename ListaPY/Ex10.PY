#Função – Crie uma função chamada saudar(nome) que receba um nome e exiba: 
#Olá, NOME! Seja bem-vindo(a)! 
#Chame a função 3 vezes pedindo nomes ao usuário.

def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

for i in range(3):
    usuario = input("Digite um nome: ")
    saudacao(usuario)
