programa {
  funcao inicio() 
  {
    real valor

    escreva("Digite um número: ")
    leia(valor)

    se (valor % 2 == 0)
    {
      escreva("O número ", valor, " é par!")
    }
    senao
    {
      escreva("O número ", valor, " é ímpar!")
    }
  }
}
