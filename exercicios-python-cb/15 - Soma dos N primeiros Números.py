#Atividade 15: Soma dos N primeiros Números

n = int(input("Digite um número: "))

total = 0
for i in range(1, n + 1):
    total += i

print(f"A soma dos primeiros {n} números naturais é: {total}")    