films = {
    "Godfather": [18, 5],
    "Wonder Woman": [15, 3],
    "Batman": [3, 5],
    "Space Jam 2": [12, 5]
}

while True:
    choice = input("Choose a movie: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())
        # Check user age
        if age >= films[choice][0]:
            # Check enough seats
            seats = int(input("How many seats?: ").strip())
            if seats <= films[choice][1]:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1]-seats
            else:
                print("Sorry, we are sold out!")
        else:
            print("Not yet, Padawaan! You are too young.")
    else:
        print("We don't have that film...")
