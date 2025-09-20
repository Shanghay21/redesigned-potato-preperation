import random


weiterspielen = True

while(weiterspielen == True):
    number = random.randint(1, 6)
    print("Es wurde die Zahl ", number, " gewürfelt!")
    retry = input("Möchtest du weiterspielen? (ja, nein): ")
    retry = str(retry)

    if retry == "ja":
        weiterspielen = True

    else:
        weiterspielen = False

