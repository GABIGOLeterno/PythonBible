'''import random

nome1 = str(input("Digite o nome 1: ".strip()))
nome2 = str(input("Digite o nome 2: ".strip()))
nome3 = str(input("Digite o nome 3: ".strip()))
nome4 = str(input("Digite o nome 4: ".strip()))

nomes = [nome1, nome2, nome3, nome4]
escolha = random.choice(nomes)
print("O aluno escolhido foi {}.".format(escolha))'''

import random

nomes = input("Digite quatro nomes: ".strip())
lista = nomes.split()
print(lista)
escolha = random.choice(lista)
print(escolha)
