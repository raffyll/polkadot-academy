#Atividade 17: Verificação de Número Perfeito

def verificacao(n):
    soma = 0

    for i in range(1, n):
        if n % i == 0:
            soma += i
    
    if soma == n:
        print(f"{n} é um número perfeito.")
    else:
        print(f"{n} não é um número perfeito.")

num = int(input("Digite um número para verificar se é perfeito: "))
verificacao(num)