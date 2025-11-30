#Repetição – Peça 5 números ao usuário usando um for e mostre:
# A soma total
 #A média dos números

soma = 0
for c in range(0,5):
 
    
    n = int(input("Digite um valor: "))

    soma += n
   

media = soma/5

print(f"A soma de todos os valores é de: {soma}")

print(f"A média é: {media:.2f}")