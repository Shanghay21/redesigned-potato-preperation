import random

password_length = input("Wie lange soll das Passwort sein? (6, 9 oder 12 Zeichen): ")
password_length = int(password_length)

if password_length == 6:
    
    small_letters = random.choice("abcdefghijklmnopxrstuvwxyz")
    tall_letters = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = random.randint(0, 9)
    small_letters2 = random.choice("abcdefghijklmnopxrstuvwxyz")
    tall_letters2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers2 = random.randint(0, 9)

elif password_length == 9:
    
    small_letters = random.choice("abcdefghijklmnopxrstuvwxyz")
    tall_letters = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = random.randint(0, 9)
    small_letters2 = random.choice("abcdefghijklmnopxrstuvwxyz")
    tall_letters2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers2 = random.randint(0, 9)
    small_letters2 = random.choice("abcdefghijklmnopxrstuvwxyz")
    tall_letters2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers2 = random.randint(0, 9)

elif password_length == 12:
    
    small_letters = random.choice("abcdefghijklmnopxrstuvwxyz")
    tall_letters = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = random.randint(0, 9)
    small_letters2 = random.choice("abcdefghijklmnopxrstuvwxyz")
    tall_letters2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers2 = random.randint(0, 9)
    small_letters2 = random.choice("abcdefghijklmnopxrstuvwxyz")
    tall_letters2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers2 = random.randint(0, 9)
    small_letters2 = random.choice("abcdefghijklmnopxrstuvwxyz")
    tall_letters2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers2 = random.randint(0, 9)
    
password_length_4 = (small_letters, tall_letters, numbers, small_letters2, tall_letters2, numbers2) * 1

print("Your new password: ", password_length_4)


