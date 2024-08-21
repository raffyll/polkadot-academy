

inicial = int(input("Digite o número inicial: "))

final = int(input("Digite o número final: "))


def e_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in range(inicial, final + 1):
    if e_primo(num):
        print(num, end='-')



