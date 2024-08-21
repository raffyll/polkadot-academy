soma = 0
num = None

while True:
    num = int(input("Digite um número para somar: (digite 0 para terminar)"))
    if num == 0:
        break
    soma += num

print(f"A soma dos números digitados é: {soma}")