#Atividade 11: Cálculo de Área de Círculo
import math

def calculo(r):
    area = math.pi * r ** 2
    return area

while True:

    try:
        r = float(input("Digite o valor do raio: "))
        area = calculo(r)
        print(f"O valor da área é: {area:.2f}")
        break
    except ValueError:
        print("Por favor, digite um número válido")
