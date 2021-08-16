valor = float(input("Qual o preço do produto? R$ ".strip()))

#Aplicar desconto de 5%
novovalor = valor * 0.95
print ("O valor original é R${:.2f}. Aplicado o desconto de 5%, o valor fica R${:.2f}.".format(valor, novovalor))
