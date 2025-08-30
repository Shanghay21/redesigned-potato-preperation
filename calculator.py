# Das ist ein Kommentar

print("Gebe hier deine Rechnung ein: ")

# Eingabe der ersten Zahl
number1 = input()
number1 = int(number1)

# Eingabe der Art
factor = input("Gebe hier den Rechenoperator ein (+, -, *, /): ")
factor = str(factor)

if factor == "+":
    print(number1, " + ")
    number2_addition = input("Gebe hier die zweite Zahl ein: ")
    number2_addition = int(number2_addition)
    print("Das Ergebnis ist: ", number1 + number2_addition)

elif factor == "-":
    print(number1, " - ")
    number2_subtraction = input("Gebe hier die zweite Zahl ein: ")
    number2_subtraction = int(number2_subtraction)
    print("Das Ergebnis ist: ", number1 - number2_subtraction)

elif factor == "*":
    print(number1, " * ")
    number2_multiplication = input("Gebe hier die zweite Zahl ein: ")
    number2_multiplication = int(number2_multiplication)    
    print("Das Ergebnis ist: ", number1 * number2_multiplication)

else:
    print(number1, " / ")
    number2_division = input("Gebe hier die zweite Zahl ein: ")
    number2_division = int(number2_division)    
    print("Das Ergebnis ist: ", number1 / number2_division)

