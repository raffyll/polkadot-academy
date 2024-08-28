# Desvendando o Código Secreto da Polkadot

## Explicação do desafio

**Objetivo:** Desenvolver um programa em Python que aplique conceitos de lógica e programação para resolver um problema de decifração de códigos utilizando laços de repetição e condicionais. Neste desafio, você ajudará a Polkadot a proteger suas transações criptográficas ao decifrar um código que protege os fundos em DOT, a moeda digital da rede Polkadot.

**Instruções:** Você foi contratado pela equipe de segurança digital da Polkadot para ajudar a decifrar um código secreto que protege as transações em DOT. O código foi gerado por um algoritmo que segue regras específicas para somar ou subtrair números dentro de um intervalo. Sua missão é criar um programa em Python que possa decifrar esse código aplicando as regras fornecidas.

**Regras do Desafio:**

 1. Dado um intervalo de números inteiros, você deverá percorrer todos os números desse intervalo.
 2. Se um número for múltiplo de 3, ele deverá ser somado ao total.
 3. Se um número for múltiplo de 5, ele deverá ser subtraído do total.
 4. Se um número for múltiplo de 3 e 5 ao mesmo tempo, ele deverá ser ignorado.
 5. No final, o programa deverá exibir o valor total calculado, representando a segurança do fundo em DOT.

# Código

    inicial = int(input("Digite o número inicial do intervalo: "))
    final = int(input("Digite o número final do intervalo: "))
        
    total = 0
        
    for i in range(inicial, final + 1):
	    if i % 3 == 0 and i % 5 == 0:
		    continue
    elif i % 3 == 0:
	    total += i
    elif i % 5 == 0:
	    total -= i
    
	print(total)
## Explicação do código

    inicial = int(input("Digite o número inicial do intervalo: "))
    final = int(input("Digite o número final do intervalo: "))
***
Puxa o valor inicial e final do intervalo da busca.

    for i in  range(inicial, final + 1):
Inicia uma iteração com o valor inicial e final recebido do usuário.
***
    if  i % 3 == 0 and i % 5 == 0:
	    continue
Se o número atual da iteração for múltiplo de 3 e 5 ao mesmo tempo, é ignorado.
***
    elif i % 3 == 0:
		total += i
Se o número atual da iteração é múltiplo de 3, é somado ao valor total.
***
    elif i % 5 == 0:
	    total -= i
Se o número atual da iteração é múltiplo de 5, é diminuído do valor total.
***
    print(total)
Imprime o valor resultante.




