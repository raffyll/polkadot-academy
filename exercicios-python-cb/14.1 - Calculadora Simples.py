#Atividade 14: Calculadora simples

print('-'*25)
print("Calculadora muito simples")
print('-'*25)

while True:
    try:
        res = input("Digite o número da operação para escolher:\n1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Sair\n")

        if res not in {"1", "2", "3", "4", "5"}:
            print("Por favor, escolha um dos números válidos.")
            continue

        if res == "5":
            break

        a = int(input("Digite um número: "))
        b = int(input("Digite outro número: "))

        if res == "1":
            resultado = a + b
            print(f"{a} + {b} = {resultado}")

        elif res == "2":
            resultado = a - b
            print(f"{a} - {b} = {resultado}")

        elif res == "3":
            resultado = a * b
            print(f"{a} x {b} = {resultado}")

        elif res == "4":
            if b == 0:
                print("Não é possível dividir por 0.")
                continue
            resultado = a / b
            print(f"{a} ÷ {b} = {resultado}")
        
    except ValueError:
        print("Digite um número válido")
        continue
    
