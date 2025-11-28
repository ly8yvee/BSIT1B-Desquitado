import os
import json

os.system('cls')
print('THE MENU - FASHION STYLE RECOMMENDER')
print('====================================')

dress_styles = {
    "Y2K": "Low-rise jeans, butterfly clips, graphic tees",
    "Stargirl": "Bright colors, quirky accessories, statement jewelry",
    "Scandi": "Minimalist, neutral tones, clean cuts",
    "Indie": "Vintage band tees, layered clothing, thrifted items",
    "Old Money": "Classic blazers, pearls, tailored trousers",
    "Alt": "Dark colors, leather jackets, band merchandise",
    "Downtown": "Streetwear, sneakers, hoodies",
    "Cottagecore": "Floral dresses, cozy knits, earthy tones"
}

user_records = {}

while True:
    os.system('cls')
    print("THE MENU - CHOOSE FROM THE FOLLOWING OPTIONS")
    print('A - ADD USER INFO & GET STYLE RECOMMENDATION')
    print('B - VIEW ALL USER RECORDS')
    print('C - SEARCH USER RECORD')
    print('D - DELETE USER RECORD')
    print('E - EDIT USER RECORD')
    print('F - EXPORT USER RECORDS')
    print('G - EXIT THE MENU')

    choice = input('SELECT FROM THE OPTIONS ABOVE ---> ').lower()

    if choice == 'a':
        os.system('cls')
        print('\n🔥 ADDING USER INFO & GETTING STYLE RECOMMENDATION 🔥')
        
        name = input('👤 Please input your FULL NAME ---> ').upper()
        age = eval(input('🎂 Please input your AGE ---> '))
        gender = input('♀️♂️ Please input your GENDER (M/F/O) ---> ').upper()
        height = input('📏 Please input your HEIGHT (ex: 5\'6") ---> ')
        occasion = input('🎉 What OCCASION is this for? (ex: school, party, casual) ---> ').title()
        
        print('\n✨ CHOOSE YOUR FAVORITE FASHION STYLE:')
        for i, style in enumerate(dress_styles, 1):
            print(f'{i}. {style}')
        
        selected_style = input('\nEnter your style choice (ex: Y2K, Scandi) ---> ').title()
        
        if selected_style in dress_styles:
            recommendation = dress_styles[selected_style]
            user_id = f"{name[:3]}{age}{len(user_records)+1}"
            
            user_records[user_id] = [name, age, gender, height, occasion, selected_style, recommendation]
            
            print(f'\n🎉 PERFECT MATCH FOUND! 🎉')
            print(f'👗 YOUR STYLE: {selected_style}')
            print(f'👠 OUTFIT RECOMMENDATION: {recommendation}')
            print(f'\n💾 DATA SAVED SUCCESSFULLY!')
            print(f'🆔 YOUR USER ID: {user_id}')
            print(f'📋 FULL PROFILE: {name}, {age}yo, {gender}, {height}, for {occasion}')
        else:
            print('❌ STYLE NOT IN THE MENU! Please choose: Y2K, Stargirl, Scandi, Indie, Old Money, Alt, Downtown, Cottagecore')
        input('\nPress Enter to continue...')
        continue

    elif choice == 'b':
        os.system('cls')
        print('👥 ALL USER RECORDS')
        if user_records:
            for user_id, info in user_records.items():
                print(f'\n🆔 ID: {user_id}')
                print(f'👤 NAME: {info[0]}')
                print(f'🎂 AGE: {info[1]} | ♀️ GENDER: {info[2]} | 📏 HEIGHT: {info[3]}')
                print(f'🎉 OCCASION: {info[4]}')
                print(f'👗 STYLE: {info[5]} | 👠 OUTFIT: {info[6]}')
                print('═' * 60)
        else:
            print('😢 NO RECORDS FOUND YET!')
        input('\nPress Enter to continue...')
        continue

    elif choice == 'c':
        os.system('cls')
        print('🔍 SEARCH USER RECORD')
        search_id = input('Enter User ID to search ---> ').upper()
        
        if search_id in user_records:
            info = user_records[search_id]
            print("=========================================")
            print(f'✅ RECORD FOUND FOR ID: {search_id}')
            print(f'👤 NAME: {info[0]}')
            print(f'🎂 AGE: {info[1]} | ♀️ GENDER: {info[2]}')
            print(f'📏 HEIGHT: {info[3]} | 🎉 OCCASION: {info[4]}')
            print(f'👗 STYLE: {info[5]}')
            print(f'👠 RECOMMENDATION: {info[6]}')
            print("=========================================")
        else:
            print('❌ NO RECORD FOUND!')
        input('\nPress Enter to continue...')
        continue

    elif choice == 'd':
        os.system('cls')
        print('🗑️ DELETE USER RECORD')
        search_id = input('Enter User ID to delete ---> ').upper()
        
        if search_id in user_records:
            info = user_records[search_id]
            print("=========================================")
            print(f'FOUND: {info[0]} | STYLE: {info[5]}')
            print("=========================================")
            confirm = input('Are you sure? (y/n): ').lower()
            if confirm == 'y':
                user_records.pop(search_id)
                print('✅ RECORD DELETED!')
            else:
                print('❌ Cancelled.')
        else:
            print('❌ NO RECORD FOUND!')
        input('\nPress Enter to continue...')
        continue

    elif choice == 'e':
        os.system('cls')
        print('✏️ EDIT USER RECORD')
        search_id = input('Enter User ID to edit ---> ').upper()
        
        if search_id in user_records:
            info = user_records[search_id]
            print("=========================================")
            print(f'CURRENT: {info[0]}, {info[1]}yo, {info[5]} style')
            print("=========================================")
            
            new_name = input('New FULL NAME ---> ').upper()
            new_age = eval(input('New AGE ---> '))
            new_gender = input('New GENDER (M/F/O) ---> ').upper()
            new_height = input('New HEIGHT ---> ')
            new_occasion = input('New OCCASION ---> ').title()
            
            print('\nCHOOSE NEW STYLE:')
            for style in dress_styles:
                print(f'- {style}')
            new_style = input('New style ---> ').title()
            
            if new_style in dress_styles:
                new_recommendation = dress_styles[new_style]
                user_records[search_id] = [new_name, new_age, new_gender, new_height, new_occasion, new_style, new_recommendation]
                print(f'\n✅ UPDATED SUCCESSFULLY!')
                print(f'👗 NEW STYLE: {new_style}')
            else:
                print('❌ Invalid style!')
        else:
            print('❌ NO RECORD FOUND!')
        input('\nPress Enter to continue...')
        continue

    elif choice == 'f':
        print('💾 EXPORTING TO JSON...')
        with open('the_menu_records.json', 'w') as new_file:
            json.dump(user_records, new_file, indent=4)
        print('\n✅ EXPORTED to the_menu_records.json!')
        input('\nPress Enter to continue...')
        continue

    elif choice == 'g':
        print('👋 THANKS FOR USING THE MENU! 💅')
        break

    else:
        print('❌ INVALID CHOICE! Choose A-G only.')
        input('\nPress Enter to continue...')
        continue
