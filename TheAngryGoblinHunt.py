import random

number_of_doors = 5

print("Welcome to the Angry Goblin Hunt")
print("An award-winning game full of adventure and excitement (!)")

# Eingabe des Benutzernamens
player_name = input ("Type in your name:")
print(player_name + ", do you think you can find the goblin hiding in the kitchen cupboards?")
print("|_|" * number_of_doors)

# Position des Goblins
goblin_position = random.randint(1, number_of_doors) 

keep_trying = True

# Eingabe der Cup-Nummer
while keep_trying:
    
    input_cup = input("Which cupboard do you think the goblin is in [type in number]:")
    input_cup = int(input_cup)

    if input_cup == goblin_position:
        print("Well done!! You have found the goblin. He was so scared he ran away.")
        keep_trying = False

    elif input_cup == goblin_position + 1:
        print("Almost! The goblin must be near. You can sense his presence!.")

    elif input_cup == goblin_position - 1:
        print("Almost! The goblin must be near. You can sense his presence!.")

    else:
        print("Sorry! The goblin is still lurking somewhere else.")

print("Game over. Thanks " + player_name + " for playing! Now get back to work!")