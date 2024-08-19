#Atividade 8: Sequência de Fibonacci

n = int(input("Digite um número de valores para ver a sequência Fibonacci:'\n"))
print("A ordem Fibonacci:")
a = 0
b = 1

for _ in range(n):
        print(a, "-> ",end='')
        a, b = b, a + b

print(f"Essa é a sequência Fibonacci até o {n}° número.")