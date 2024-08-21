#Atividade 3: Cálculo de IMC

altura = float(input("Qual a sua altura em metros?"))

peso = int(input("Quantos kg você pesa?"))

imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.2f}")  