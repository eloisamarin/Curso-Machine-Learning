#  Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.

def elementos_unicos(lista1, lista2):

    return [item for item in lista1 if item not in lista2] + [item for item in lista2 if item not in lista1]

def f():
    while True:
        try:
            vezes1 = int(input("Quantos números você vai digitar para a primeira lista?"))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    lista1 =  []

    for i in range(vezes1):
        while True:
            try:
                numero = int(input("Digita o número: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
        lista1.append(numero)
    
    while True:
        try:
            vezes2 = int(input("Quantos números você vai digitar para a segunda lista?"))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    lista2 =  []

    for i in range(vezes2):
        while True:
            try:
                numero = int(input("Digita o número: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
        lista2.append(numero)
    
    return elementos_unicos(lista1, lista2)
print("Elementos únicos:", f())