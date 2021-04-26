estudantes = {
              "Gabigol": {"id":"ID01", "age":23, "grade":"A"},
              "Arão": {"id": "ID02", "age": 27, "grade":"B"},
              "Jj": {"id":"ID03", "age": 67, "grade":"C"},
              "Arrasca": {"id": "ID04", "age":25, "grade":"D"},
              "Diego": {"id":"ID05", "age":35, "grade":"E"}
              }

while True:
    user = input("Type name or id: ").strip()
    if user in estudantes.keys():
        ask = str(input("id, age, grade or all?: ").strip())
        if ask == "all":
            print(estudantes[user])
        elif ask == "id" or "age" or "grade":
            print(estudantes[user][ask])
    else:
        print(user, "not found.")
