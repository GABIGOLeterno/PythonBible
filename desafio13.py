salario = float(input("Digite o salário bruto: R$".strip()))

#Aplicar 15% de aumento
novosalario = salario * 1.15
print ("Salário atual:R${:.2f}; salário com aumento de 15%: r${:.2f}".format(salario, novosalario))