#Atividade 7: Média de Notas

números = []
i = 0
total = 0
soma = 0

while True:

    try:
        i = int(input("Digite um número para adicionar a média. Para ver o resultado digite: -1\n"))
        if i == -1:
            break
        soma = i
        total += soma 
        números.append(i)
        
    except ValueError:
        print("Por favor, digite um número válido!")
           
resultado = total / len(números)
print(f"A média {total} / {len(números)} dos números digitados é: {resultado}") 