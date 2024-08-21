#Atividade 18: Contagem de Palavras

frase = input("Digite uma frase: ")

palavras = frase.split()
total = len(palavras)

print(f"A sua frase tem {total} palavras.")