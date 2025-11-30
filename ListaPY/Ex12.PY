#Função + Dicionário + Repetição - Crie uma função cadastrar_pessoa() que: 
#• Peça nome 
#• Peça idade 
#• Peça cidade 
#• Retorne um dicionário com esses dados 
#No programa principal: 
#• Use um while para cadastrar várias pessoas 
#• Cada pessoa deve ser guardada dentro de uma lista de dicionários 
#• Pare quando o usuário digitar “sair” 
# Ao final, exiba todos os cadastros organizados

def cadastrar():
    nome = input("Nome: ")
    idade = input("Idade: ")
    cidade = input("Cidade: ")
    
    return {
        "Nome": nome,
        "Idade": idade,
        "Cidade": cidade
    }


cadastros = []

while True:
    opcao = input("\nPressione ENTER para cadastrar ou digite 'sair' para encerrar: ").lower()
    
    if opcao == "sair":
        break
    
    pessoa = cadastrar()
    cadastros.append(pessoa)


print("\n=== Lista de Cadastros ===")

for i in range(1, len(cadastros) + 1):
    pessoa = cadastros[i - 1]   
    print(f"\nCadastro {i}:")
    print(f"  Nome:   {pessoa['Nome']}")
    print(f"  Idade:  {pessoa['Idade']}")
    print(f"  Cidade: {pessoa['Cidade']}")