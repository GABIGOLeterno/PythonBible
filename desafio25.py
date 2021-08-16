while True:
    nome = str(input("Digite seu nome: ").strip())
    nome2 = nome.lower()
    print("Você tem Silva no nome? {}.".format("silva" in nome2))