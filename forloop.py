vowels = 0
consoantes = 0

for letter in "Hello":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consoantes = consoantes + 1

print("Há {} vogais.".format(vowels))
print("Há {} consoantes.".format(consoantes))
