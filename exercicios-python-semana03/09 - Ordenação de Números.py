#Atividade 9: Ordenação de Números

lista = []
num = 3

for i in range(num):
    valor = int(input("Digite um número para ser listado: "))
    lista.append(valor)

lista.sort()
print(lista)