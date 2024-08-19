#Atividade 20: Análise de Lista de Números

lista = []
n = 0

try:

    n = int(input("Digite quantos números você deseja adicionar na lista: "))

    for i in range(n):
            num = int(input("Digite um número para adicionar: "))
            lista.append(num)

    if len(lista) == 0:
        print("A lista está vazia!")        
    else:   
        menor = min(lista)
        maior = max(lista)
        media = sum(lista) / len(lista)

    print(f"O menor valor da lista é {menor}, o maior valor é {maior}, e a média de todos os valores é: {media}")

except ValueError:
    print("Por favor, digite um número válido.")    