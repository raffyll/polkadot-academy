programa {
  funcao inicio() 
  {
    real celsius, fahrenheit

    escreva("Digite a temperatura em Celsius: ")
    leia(celsius)

    fahrenheit = (celsius * 9/5) + 32

    escreva(celsius, "°C em Celsius equivalem a ", fahrenheit, "°F em Fahrenheit.")
  }
}
