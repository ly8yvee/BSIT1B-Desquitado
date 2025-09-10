print("Welcome to the Manga Hub Reader!")
print("Answer a few questions to find your next read.")

d = input("What genre do you like? (action, romance, horror)--->").strip()
a = input("How should the manga be? (short, medium, long)--->").strip()
k = input("Which decade? (2000, 2020)--->").strip()

if d == 'romance':
   if a == 'long':
      if k == '2003':
         print("We recommend: Sand Chronicles")

else:
        print("No long romance manga available right now.")

if d == 'romance':
   if a == 'short':
      if k == '2005':
         print("We recommend: Solanin")
else:
        print("No short romance manga available right now.")

if d == 'romance':
   if a == 'medium':
      if k == '2007':
         print("We recommend: Horimiya")
else:
        print("No medium romance manga available right now.")

if d == 'action':
   if a == 'short':
      if k == '2014':
         print("We recommend: All You Need is Kill by Takeshi Obata")
else:
         print("No short action manga available right now.")

if d == 'action':
   if a == 'medium':
      if k == '2010':
         print("We recommend: Akame ga Kill")
else:
         print("No medium action manga available right now.")

if d == 'action':
   if a == 'long':
      if k == '2007':
         print("We recommend: Psyren")
else:
         print("No long action manga available right now.")


if d == 'horror':
   if a == 'medium':
      if k == '2009':
         print("We recommend: I Am a Hero")
else:
         print("No medium horror manga available right now.")

if d == 'horror':
   if a == 'long':
      if k == '2011':
         print("We recommend: Tokyo Ghoul + Tokyo Ghoul:re")
else:
         print("No long horror manga available right now.")

if d == 'horror':
   if a == 'short':
      if k == '2009':
         print("We recommend: I Am a Hero")
else:
         print("No short horror manga available right now.")

