programa {
  funcao inicio() 
  {
    inteiro valor

    escreva("Digite um número para ver a tabuada: ")
    leia(valor)

    para (inteiro i = 1; i <= 10; i++)
    {
      escreva(valor, " x ", i, " = ", valor * i,"\n")
    }

  }
}
