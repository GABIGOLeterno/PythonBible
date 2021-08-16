while True:
    frase = input("Escreva uma frase: ").strip()
    frase2 = frase.lower()
    print("A letra A apareceu {} vezes.".format(frase2.count("a")))
    print("A primeira letra A apareceu na posição {}.".format(frase2.find("a")+1))
    print("A última letra A apareceu na posição na posição {}.".format(frase2.rfind("a")+1))