import random

contagem = 0
numeros = []
tentados = []

for i in range(5):
    numeros.append(random.randint(1,75))

print('-'*51)
print("Bingo da Polkadot - Adivinhe os 5 números de 1 a 75")
print('-'*51)

while True:

    try:

        if len(numeros) == 0:
            break
        tentativa = int(input("Digite um número para tentar:"))
        if tentativa <= 0 or tentativa > 75:
            print("Digite um número entre 1 e 75, por favor.")
            continue
        if tentativa in tentados:
            print("Você já digitou este número! Tente novamente!")
            continue
        tentados.append(tentativa)
        contagem += 1
        print("Números já tentados: ", tentados)
        if tentativa in numeros:
            numeros.remove(tentativa)
            print(f"Você acertou! O número era {tentativa}, faltam {len(numeros)}!")
                     
    except ValueError:
        print("Por favor, digite um número inteiro.")

print(f"Parabéns, você ganhou com {contagem} tentativas!")
