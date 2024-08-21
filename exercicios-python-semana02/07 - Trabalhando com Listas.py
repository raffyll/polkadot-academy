lista = []

while True:
    add = str(input("Adicione itens a sua lista (digite 0 para encerrar):  "))
    if add == "0":
        break
    lista.append(add)


print(f"Aqui está a sua lista: ")
for itens in lista:
    print(itens)