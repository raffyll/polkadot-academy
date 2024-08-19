#Atividade 14: Calculadora Simples

print('-'*50)
print("Calculadora simples para quem não gosta de números")
print('-'*50)

def soma(a, b):
    resultado = a + b
    return resultado

def subtraçao(a, b):
    resultado = a - b
    return resultado

def multiplicaçao(a, b):
    resultado = a * b
    return resultado

def divisao(a, b):
    if b == 0:
        return "Não é permitido dividir por zero."
    resultado = a / b
    return resultado

def resposta(tipo, a, b, resultado):
    print(f"A {tipo} de {a} e {b} é igual a: {resultado}")

while True:
    
    try:

        tipo = input("Que tipo de conta deseja fazer? (soma - subtração - multiplicação - divisão)\n").casefold()
        a = int(input("Digite um valor: "))
        b = int(input("Digite outro valor:"))

        if tipo == "soma":
            resultado = soma(a, b)
            resposta(tipo, a, b, resultado)
            break
        elif tipo == "subtração":
            resultado = subtraçao(a, b)
            resposta(tipo, a, b, resultado)
            break
        elif tipo == "multiplicação":
            resultado = multiplicaçao(a, b)
            resposta(tipo, a, b, resultado)
            break
        elif tipo == "divisão":
            resultado = divisao(a, b)
            resposta(tipo, a, b, resultado)
            break
        else:
            print("Digite o tipo corretamente.")
                           
    except ValueError:
        print("Por favor, digite um número válido.")            