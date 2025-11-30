#Match Case – Crie um menu usando match case:
#1 - Olá
#2 - Informações
#3 - Sair

op = int(input("Escolha uma das opções abaixo:\n 1 - 'Óla'\n 2 - Informaçoes\n 3 - 'Sair'"))

match op:

    case 1: 
        print("Olá")
    case 2:
        print("Informações")
    case 3: 
        print("Saindo do Programa...")