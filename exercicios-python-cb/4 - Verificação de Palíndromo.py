#Atividade 4: Verificação de Palíndromo

base = input("Digite uma palavra ou frase(sem pontuação) para verificar se é um palíndromo: ")
formato = base.casefold()
espaço = formato.replace(' ','')
invertida = espaço[::-1]

if invertida == espaço:
    print(f"É um palíndromo: {espaço} -- {invertida}.")
else:
    print(f"Não é um palíndromo: {espaço} -- {invertida}.")
        