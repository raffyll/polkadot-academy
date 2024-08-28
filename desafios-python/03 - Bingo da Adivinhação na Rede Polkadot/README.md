# Bingo da Adivinhação na Rede Polkadot

## Explicação do desafio

**Objetivo:** Desenvolver um programa em Python que simule um jogo de bingo. Neste caso, a cartela representa uma carteira de DOT, e você precisará adivinhar os números para completar a transferência segura.

**Contexto:** : Você foi encarregado de criar uma versão digital de um jogo de bingo para a comunidade Polkadot. No Bingo da Adivinhação, o computador sorteia números aleatórios, e você deverá tentar adivinhar os números sorteados para completar sua carteira de DOT. Quem conseguir adivinhar todos os números da sua cartela primeiro garante a transferência segura dos seus fundos.

**Regras do Desafio:**

1. O programa deverá gerar uma cartela de bingo para você, composta por 5 números aleatórios diferentes entre 1 e 75.
 2. O computador sorteará números aleatórios, um de cada vez.
 3. Você deverá adivinhar quais números foram sorteados.
 4. Se você acertar um número, ele será marcado na cartela (removido da lista).
 5. O jogo continua até que você complete todos os números da cartela.
 6. O programa deverá contar e exibir o número total de sorteios necessários para completar a cartela.
 
 # Código

    import  random 
      
    print('-'*51)
    print("Bingo da Polkadot - Adivinhe os 5 números de 1 a 75")
    print('-'*51)
      
    contagem = 0
    cartela = []
    sorteados = []
    sorteio =  None
    
    for i in range(5):
	    cartela.append(random.randint(1,75))
     
    print(f"Sua cartela inicial: {cartela}") 
    print('-'*51)
    
    while True:
    
	    if len(cartela) == 0:
		    break    
	    sorteio = random.randint(1,75)    
	    if sorteio in sorteados:
		    continue
	    sorteados.append(sorteio)
	    print(f"Número sorteado: {sorteio}")
		contagem += 1    
	    if sorteio in cartela:
			cartela.remove(sorteio)    
		    print(f"Você acertou o número {sorteio}! Números restantes na cartela: {cartela}")          
    
    print(f"Parabéns! Você ganhou com {contagem} sorteios.")

## Explicação do código

	for i in range(5):
	    cartela.append(random.randint(1,75))
Faz uma iteração e adiciona 5 números aleatórios de 1 a 75 na array cartela usando o módulo random.
***
	print(f"Sua cartela inicial: {cartela}") 
Mostra a sua cartela inicial.
***
	while True:
Cria um loop infinito que só é parado até que alguma condição seja atendida.
***
	if len(cartela) == 0:
		    break    
Se a array "cartela" estiver vazia quebra o loop.
***
	sorteio = random.randint(1,75)    
A variável "sorteio" recebe um número aleatório também usando o módulo random.
***
	if sorteio in sorteados:
		    continue
Se o número sorteado já estiver dentro da array "sorteados", que contém os números já foram, a iteração é ignorada e reiniciada.
***
	sorteados.append(sorteio)
Adiciona o número sorteado ao array que guarda os novos números para evitar repetição.
***
	print(f"Número sorteado: {sorteio}")
		contagem += 1    
Mostra ao usuário o número sorteado e adiciona 1 tentativa a contagem total.
***
	if sorteio in cartela:
			cartela.remove(sorteio)    
		    print(f"Você acertou o número {sorteio}! Números restantes na cartela: {cartela}") 
Se o usuário tiver o número sorteado na cartela, ele é removido da lista faltante,  imprime o número acertado e mostra os números restantes.
***
	print(f"Parabéns! Você ganhou com {contagem} sorteios.")
Ao final, mostra quantos sorteios foram necessários para terminar o bingo.

