#Atividade 2: Conversão de Temperaturas

celsius = float(input("Digite uma temperatura em Celsius:"))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius}°C Celsius equivalem a {fahrenheit}°F em Fahrenheit e {kelvin}K em Kelvin.")