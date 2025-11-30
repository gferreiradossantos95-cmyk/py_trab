# Listas – Com uma lista contendo 8 frutas, peça ao usuário uma fruta e diga se ela está na lista
#usando operador in.


frutas = ["Abacate","Banana","Uva","Uva","Limão","Maçã","Ameixa","Laranja","Morango"]

fruta = input("Escolha uma fruta: ")

for c in frutas:
    if fruta not in frutas:
        print("esta fruta não está na lista!")


    else:
   

        print([c])
