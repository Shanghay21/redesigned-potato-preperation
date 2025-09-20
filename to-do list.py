import json

aufgabe = []

run = True

while run:

    aufgabe = input("Aufgabe einfügen: ")
    print("1. ", aufgabe)
    list = input("Möchtest du deine Liste hervorrufen? (Ja, Nein): ")
    if list == "Ja":
        print(aufgabe)

    else: 
        frage = input("Weitere Aufgabe einfügen? (Ja, Nein) Um das Programm zu stoppen bitte (stop) eingeben: ")
        if frage == "Ja":
            aufgabe = input("Aufgabe einfügen: ")

        elif frage == "stop":
            run = False
            print("Deine To-Do-Liste wurde gespeichert und geschlossen.")

        else:
            print("Aufgabe eingefügt.")


# Aufgaben in JSON speichern
with open("aufgaben.json", "w", encoding="utf-8") as f:
    json.dump(aufgabe, f, ensure_ascii=False, indent=4)

print("Deine To-Do-Liste wurde gespeichert.")

# Aufgaben wieder aus JSON laden
with open("aufgaben.json", "r", encoding="utf-8") as f:
    gespeicherte_aufgaben = json.load(f)

print("Deine gespeicherten Aufgaben:")
for i, aufgabe in enumerate(gespeicherte_aufgaben, 1):
    print(f"{i}. {aufgabe}")