#Atividade 12: Jogo de Adivinhação
import random

num = random.randint(1,100)

print('-'*60)
print("Jogo da Adivinhação -- Tente acertar o número de 1 a 100!")
print('-'*60)

while True:

    try:

       valor = int(input("Digite um número: "))
       if valor == num:
           print(f"Parabéns! Você acertou o número! O número era: {num}")
           break
       elif valor < num:
           print(f"O número é maior que {valor}. Tente novamente!")
       else:
           print(f"O número é menor que {valor}. Tente novamente!")
    except ValueError:
        print("Por favor, digite um número válido.")   