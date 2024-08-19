#Atividade 1: Calculando o fatorial

fatorial = 1
valor = int(input("Digite um número: "))
i = valor
while i >= 1:
    fatorial = i * fatorial
    i -= 1

print(f"A fatorial de {valor} é: {fatorial}")
