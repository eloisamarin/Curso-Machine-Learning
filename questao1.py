#  Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares

def f():
    while True:
        try:
            vezes = int(input("Quantos números você vai digitar?"))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    lista =  []

    for i in range(vezes):
        while True:
            try:
                numero = int(input("Digita o número: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
        lista.append(numero)
    
    listaimpares = [num for num in lista if num % 2 != 0]
    return listaimpares
print(f())
