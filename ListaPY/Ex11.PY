#Função + Lista – Crie uma função chamada calcular_media(lista_notas). A função deve 
#retornar a média dos valores. 
#No programa principal: 
#• Peça 4 notas ao usuário 
#• Coloque numa lista 
#• Use a função para calcular a média 
#• Exiba o resultado 


def media(notas):
    return sum(notas) / len(notas)


notas = []


for i in range(4):
    nota = float(input(f"Informe a {i+1}ª nota: "))
    notas.append(nota)


media = media(notas)


print(f"\nA média das notas é: {media:.2f}")
