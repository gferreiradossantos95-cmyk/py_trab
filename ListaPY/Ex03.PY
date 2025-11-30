#Listas – Cadastro Simples (Fácil)
#Peça nomes ao usuário e adicione em uma lista.
#O programa deve parar quando o usuário digitar "sair".
#Ao final, exiba:
#• Quantos nomes foram cadastrados
#• A lista completa

nomes = []


while True:
    nome = input("Informe um nome para adicionar a lista: (ou digite 'sair' para sair): ")

    if nome == 'sair':
        break
    
    if nome:
        nomes.append(nome)

print(f"A quantidade de nomes adicionados é de: {len(nomes)}\n")
print(f"{nomes}")
