frase = str(input("Digite uma frase: ")).casefold()

letra = str(input("Digite uma letra para ser contada: ")).casefold()

contagem = frase.count(letra)

print(f"A letra {letra} aparece {contagem} vezes na sua frase!")
