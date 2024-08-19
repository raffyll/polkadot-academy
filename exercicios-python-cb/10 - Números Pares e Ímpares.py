#Atividade 10: Números Pares e Ímpares

while True:

    try:

        num = int(input("Digite um número: "))
        if num % 2 == 0:
            print(f"O número {num} é par!")
            break
        else:
            print(f"O número {num} é ímpar!")
            break

    except ValueError:
        print("Por favor, digite um número inteiro.")            