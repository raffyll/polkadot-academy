inicial = int(input("Digite o número inicial do intervalo: "))

final = int(input("Digite o número final do intervalo: "))

total = 0

for i in range(inicial, final + 1):
    if i % 3 == 0 and i % 5 == 0:
        continue
    elif i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total -= i

print(total)