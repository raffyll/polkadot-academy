#Atividade 5: Tabuada

num = int(input("Digite um número para ver a tabuada: "))
for i in range(1,11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")