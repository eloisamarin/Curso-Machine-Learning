#Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.


def criarlista():
    while True:
        try:
            vezes = int(input(f"Quantos números você vai digitar para a lista? "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    numeros =  []
    for i in range(vezes):
        while True:
            try:
                numero = int(input("Digita o número: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
        numeros.append(numero)
    return numeros
def segundo_maior():
    numeros = criarlista()
    unique_numeros = list(set(numeros))  # Remove duplicates
    if len(unique_numeros) < 2:
        return None  #Não há segundo maior se não houver pelo menos dois números únicos
    unique_numeros.sort(reverse=True)
    return unique_numeros[1],numeros

segundo, lista_original = segundo_maior()
print("Lista de números:", lista_original)
print("O segundo maior número é:", segundo if segundo is not None else "Não existe segundo maior")

