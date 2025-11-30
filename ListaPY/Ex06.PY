# Tupla – Crie uma tupla com números inteiros. Peça ao usuário um número e diga:
#• Se ele está na tupla
#• Em qual posição (índice) aparece pela primeira vez

num = (1, 2, 3, 4, 5, 6, 7, 8, 9)

n = int(input("Digite um número: "))

for c in num:
    if n not in num:
        print("Este número não está na lista!")
        break
    else:
        print(f"O número digitado está na posição: {num.index(n)}")
        break