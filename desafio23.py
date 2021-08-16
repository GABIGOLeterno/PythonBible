while True:
    num = int(input("Digite um número de 1 a 9999: ").strip())
    n = str(num)
    if num in range(1,10000):
        print("Seu número é {}.".format(num))
        if len(n) == 4:
            print("Há {} milhares".format(n[0]))
            print("Há {} centenas.".format(n[1]))
            print("Há {} dezenas.".format(n[2]))
            print("Há {} unidades.".format(n[3]))
        elif len(n) == 3:
            print("Há {} centenas.".format(n[0]))
            print("Há {} dezenas.".format(n[1]))
            print("Há {} unidades.".format(n[2]))
        elif len(n) == 2:
            print("Há {} dezenas.".format(n[0]))
            print("Há {} unidades.".format(n[1]))
        elif len(n) == 1:
            print("Há {} unidades.".format(n[0]))
    else:
        print("Número inválido.")

'''unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10'''