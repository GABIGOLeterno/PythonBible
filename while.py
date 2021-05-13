l = []

while len(l) < 3:
    new_name = input("Please add a new name: ").strip().capitalize()
    l.append(new_name)

print("Sorry, list is full.")
print(l)