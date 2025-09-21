# Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das qpessoas em ordem alfabética.

def ordenar_pessoas_por_nome(pessoas):
    return sorted(pessoas, key=lambda x: x[0].lower())
def coletar_dados():
    while True:
        try:
            vezes = int(input("Quantas pessoas você vai digitar?"))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    lista =  []

    for i in range(vezes):
        while True:
            try:
                nome = input("Digite o nome: ")
                idade = int(input("Digite a idade: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para a idade.")
        lista.append((nome, idade))
    
    return ordenar_pessoas_por_nome(lista)

pessoas_ordenadas = coletar_dados()

print("Lista ordenada por nome:", pessoas_ordenadas)
for pessoa in pessoas_ordenadas:
    print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]}")