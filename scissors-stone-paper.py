import random

computer_choice = random.randint(1, 3)

keep_trying = True

while keep_trying:

    # Spieler wählt aus
    
    player_choice = input("Gib deine Wahl ein (Schere, Stein, Papier): ")

    if player_choice == "Schere":
        print("Du hast Schere gewählt")
    elif player_choice == "Stein":
        print("Du hast Stein gewählt")
    else:
        print("Du hast Papier gewählt")


    # Computer wählt aus

    if computer_choice == 1:
        print("Der Computer hat Schere gewählt")
        if player_choice == "Schere":
           print("Gleichstand!")
        elif player_choice == "Papier":
            print("Du wurdest vom Computer geschlagen!")
        else:
            print("Sieg! Du hast gegen den Computer gewonnen!")

    elif computer_choice == 2:
        print("Der Computer hat Stein gewählt")
        if player_choice == "Stein":
           print("Gleichstand!")
        elif player_choice == "Schere":
            print("Du wurdest vom Computer geschlagen!")
        else:
            print("Sieg! Du hast gegen den Computer gewonnen!")

    else:
        print("Der Computer hat Papier gewählt")
        if player_choice == "Papier":
           print("Gleichstand!")
        elif player_choice == "Stein":
            print("Du wurdest vom Computer geschlagen!")
        else:
            print("Sieg! Du hast gegen den Computer gewonnen!")
           
    # Weiterspielen?
    retry = input("Möchtest du weiterspielen? (Ja, Nein): ")
    retry = str(retry)
    if retry == "Ja":
        keep_trying = True
    else:
        keep_trying = False
    
