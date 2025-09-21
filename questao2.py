#Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

# A função deve ser capaz de lidar com entradas inválidas e solicitar novamente a entrada ao usuário.

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
    
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    listaprimos = [num for num in lista if is_prime(num)]
    return listaprimos
print("Números primos:", f())

