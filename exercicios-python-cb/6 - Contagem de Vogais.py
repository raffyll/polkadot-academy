#Atividade 6: Contagem de vogais

vogais = ['a','e','i','o','u']
frase = input("Digite uma frase: ").casefold()

num = 0

for i in frase:
    if i in vogais:
        num +=1

print(f"A frase: '{frase}' tem: {num} vogais. ")