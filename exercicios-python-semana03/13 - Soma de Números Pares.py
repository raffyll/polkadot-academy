#Atividade 13: Soma de números Pares

resultado = 0

for i in range(1,101):
    num = i
    if num % 2 == 0:
        resultado += num

print(f"O resultado da soma dos números pares de 1 a 100 é: {resultado}")        