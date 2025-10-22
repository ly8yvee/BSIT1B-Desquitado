r = []

lybag = ""

print(" --ANIME TITLES COLLECTOR!-- ")
print("Type 'done' to finish collecting. \n")

while lybag != "done":
    
    lybag = input("Enter an anime name: ")
    
    if lybag != "done":
        r.append(lybag)
        print(f"'{lybag}' has been added to your anime list.")

print("\n--- DONE COLLECTING ---")

print("Your Favorite Anime List:")
for title in r:
    print(f"- {title}")