#Atividade 19: Média Ponderada

try:

    a = float(input("Digite a primeira nota (peso 2): "))
    b = float(input("Digite a segunda nota (peso 3): "))
    c = float(input("Digite a terceira nota (peso 5): "))

    a = a * 2
    b = b * 3
    c = c * 5
    resultado = (a + b + c) / 10

    print(f"A média ponderada das três notas é: {resultado:.2f}")

except ValueError:
    print("Por favor, digite um número válido.")