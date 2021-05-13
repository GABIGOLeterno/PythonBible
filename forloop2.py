students = {
    "male": ["Jorge", "Gabriel", "Clark", "Cristo"],
    "female": ["Sarah", "Miriam", "Yael", "Roberta"]
}

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)

