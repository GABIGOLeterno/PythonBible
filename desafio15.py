dias = float(input("Dias alugados: ".strip()))
km = float(input("Kilômetros rodados: ".strip()))

#Valor a pagar
valor = float(dias * 60 + km * 0.15)
print("O valor total a ser pago é de R${:.2f}.".format(valor))
