from random import choice

pergs = ["Por que o Sol some à noite?", "Por que o Sol nasce de manhã?", "Por os judeus vão para Israel?", "Por que você tem esse nome?"]

perg = choice(pergs)
answer = input(perg).capitalize().strip()

while answer != "Porque sim":
    answer = input("Por que?: ").capitalize().strip()

print("Awesome, papito! Yeah!")
