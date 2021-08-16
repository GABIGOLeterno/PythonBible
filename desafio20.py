import random

nomes = input("Digite os nomes que apresentarão os trabalhos: ".strip())
lista = nomes.split()
random.shuffle(lista)
print("A ordem das apresentações será:")
print (lista)
