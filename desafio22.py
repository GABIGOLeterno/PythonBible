nome = str(input("Digite seu nome: ").strip())

mai = nome.upper()
print("Seu nome em maiúscula é: {}.".format(mai))
min = nome.lower()

print("Seu nome em minúsucla é: {}.".format(min))
print("Seu nome tem {} caractéres.".format(len(nome) - nome.count(' ')))

# print("Seu primeiro nome tem {} letras.".format(nome.find(' ')))
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras.".format(separa[0], len(separa[0])))

