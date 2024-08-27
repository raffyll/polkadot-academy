def e_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def soma_digitos(numero):
    return sum(int(digito) for digito in str(numero))

print("Digite um intervalo para procurar o número mágico da Polkadot.")
inicial = int(input("Digite o número inicial do intervalo: "))
final = int(input("Digite o número final do intervalo: "))

for numero in range(inicial, final + 1):
    if numero % 4 == 0 and e_primo(numero):
        if soma_digitos(numero) % 2 != 0:
            print(numero)
    else:
        print("O número mágico não foi encontrado.")
        break
                
