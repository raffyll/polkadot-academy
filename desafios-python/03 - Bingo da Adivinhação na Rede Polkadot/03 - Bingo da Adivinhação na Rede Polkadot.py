import random

print('-'*51)
print("Bingo da Polkadot - Adivinhe os 5 números de 1 a 75")
print('-'*51)

contagem = 0
cartela = []
sorteados = []
sorteio = None

for i in range(5):
    cartela.append(random.randint(1,75))

print(f"Sua cartela inicial: {cartela}")
print('-'*51)

while True:

    if len(cartela) == 0:
        break
    sorteio = random.randint(1,75)
    if sorteio in sorteados:
        continue
    sorteados.append(sorteio)
    print(f"Número sorteado: {sorteio}")
    contagem += 1
    if sorteio in cartela:
        cartela.remove(sorteio)
        print(f"Você acertou o número {sorteio}! Números restantes na cartela: {cartela}")                    

print(f"Parabéns! Você ganhou com {contagem} sorteios.")