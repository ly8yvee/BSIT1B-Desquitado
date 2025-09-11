print("Welcome to the Manga Hub Reader!")
print("Answer a few questions to find your next read.")

s = input("Which do you prefer? (manga or manhwa) --->").strip()
d = input("What genre do you like? (action, romance, horror)--->").strip()
a = input("How should the manga be? (short, medium, long)--->").strip()
k = input("Which decade? (2000, 2020)--->").strip()

if d == 'romance':
    if a == 'long':
        if k == '2000':
            print("We recommend: Sand Chronicles")
        else:
            print("No long romance manga available for that decade right now.")
    elif a == 'short':
        if k == '2000':
            print("We recommend: Solanin")
        else:
            print("No short romance manga available for that decade right now.")
    elif a == 'medium':
        if k == '2000':
            print("We recommend: Horimiya")
        else:
            print("No medium romance manga available for that decade right now.")
    else:
        print("Invalid length choice.")

elif d == 'action':
    if a == 'short':
        if k == '2020':
            print("We recommend: All You Need is Kill by Takeshi Obata")
        else:
            print("No short action manga available for that decade right now.")
    elif a == 'medium':
        if k == '2010':  # If you want a valid decade, update input or this check accordingly
            print("We recommend: Akame ga Kill")
        else:
            print("No medium action manga available for that decade right now.")
    elif a == 'long':
        if k == '2000':
            print("We recommend: Psyren")
        else:
            print("No long action manga available for that decade right now.")
    else:
        print("Invalid length choice.")

elif d == 'horror':
    if a == 'medium':
        if k == '2000':
            print("We recommend: I Am a Hero")
        else:
            print("No medium horror manga available for that decade right now.")
    elif a == 'long':
        if k == '2020':
            print("We recommend: Tokyo Ghoul + Tokyo Ghoul:re")
        else:
            print("No long horror manga available for that decade right now.")
    elif a == 'short':
        if k == '2000':
            print("We recommend: I Am a Hero")
        else:
            print("No short horror manga available for that decade right now.")
    else:
        print("Invalid length choice.")

else:
    print("Genre not recognized. Please choose action, romance, or horror.")
   
