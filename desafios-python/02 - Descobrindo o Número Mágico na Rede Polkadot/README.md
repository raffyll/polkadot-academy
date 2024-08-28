# Descobrindo o Número Mágico na Rede Polkadot

## Explicação do desafio

**Objetivo:** Aplicar conceitos de lógica e programação em Python para resolver um problema envolvendo números primos, operações com dígitos e condicionais. Neste desafio, você ajudará a Polkadot a descobrir um número mágico que pode desbloquear novas oportunidades de staking em DOT.

**Contexto:** Um desenvolvedor da Polkadot escondeu um número mágico na rede que pode aumentar os ganhos em staking de DOT. Esse número segue regras específicas e está escondido dentro de um intervalo de números inteiros. Sua missão é criar um programa em Python que consiga identificar esse "Número Mágico" e revelar as novas oportunidades de staking.

**Regras do Desafio:**

1. O "Número Mágico" é o primeiro número dentro de um intervalo que atende a todas as condições abaixo:
 2. É divisível por 4.
 3. É um número primo
 4. A soma dos dígitos do número é um número ímpar.
 5. Se nenhum número no intervalo atender a todas essas condições, o programa deverá informar que o "Número Mágico" não foi encontrado.
 
 # Código

    def e_primo(numero):
	    if numero < 2:
		    return False
	    for i in range(2, int(numero ** 0.5) + 1):
		    if numero % i == 0:
			    return False
	    return True
  
    def soma_digitos(numero):
	    return sum(int(digito) for digito in  str(numero)) 
    
    print("Digite um intervalo para procurar o número mágico da Polkadot.") 
    inicial = int(input("Digite o número inicial do intervalo: ")) 
    final = int(input("Digite o número final do intervalo: "))
     
    for numero in range(inicial, final + 1):
	    if numero % 4 == 0 and e_primo(numero):
		    if soma_digitos(numero) % 2 != 0:
			    print(numero)
    else: 
	    print("O número mágico não foi encontrado.")
	    break
## Explicação do código

    def e_primo(numero):
	    if numero < 2:
		    return False
	    for i in range(2, int(numero ** 0.5) + 1):
		    if numero % i == 0:
			    return False
	    return True
 Função que retorna se o número recebido é primo com um boolean.
***
    def soma_digitos(numero):
        return sum(int(digito) for digito in  str(numero)) 
        
Função que faz a soma dos dígitos do número recebido.
   ***
     inicial = int(input("Digite o número inicial do intervalo: "))       
     final = int(input("Digite o número final do intervalo: "))
Recebe o input do valor inicial e final do intervalo de busca.
***
    for numero in range(inicial, final + 1):
Faz a iteração por todos os números dentro do intervalo recebido.
***
    if numero % 4 == 0 and e_primo(numero):
		    if soma_digitos(numero) % 2 != 0:
			    print(numero)
Se o número atual da iteração é múltiplo de 4, é primo e a soma dos seus dígitos é ímpar, imprime este número.
***
    else: 
	    print("O número mágico não foi encontrado.")
	    break
Caso contrário, imprime: "O número mágico não foi encontrado." e encerra o programa.

