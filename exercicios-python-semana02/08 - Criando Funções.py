def parimpar(num):
    if num % 2 == 0:
        return print("O número é par.")
    else:
        return print("O número é ímpar.")    

numero = int(input("Digite um número: "))
parimpar(numero)