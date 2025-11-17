import os


os.system('cls')
print('STUDENT INFORMATION SYSTEM')
print('=================================')

#empty dictionary
student_record = {}

while True:
    print("STUDENT FROM THE FOLLOWING OPTIONS")
    print('A - ADD STUDENT RECORD')
    print('B - PRINT ALL STUDENT RECORD')
    print('C - SEARCH STUDENT RECORD')
    print('D - DELETE STUDENT RECORD')
    print('E - EDIT STUDENT RESCORD')
    print('F - EXPORT STUDENT RECORD')
    print('G - EXIT SYSTEM')

    choice = input('SELECT FROM THE OPTIONS ABOVE ---> ').lower()

    if choice == 'a':
        print('\nADDING STUDENT RECORD ')

        id_no = input('please input ID number ---> ')

        first_name = input('pleaase input Styudent First Name ---> ').upper()
        second_name = input('please input Student Second Name ---> ').upper()
        age = eval(input('input student age ---> '))
        course = input('input student course ---> ').upper()
        section = input('input student section ---> ').upper()

        student_record[id_no] = [first_name, second_name, age, course, section]
        print('DATA SAVED SUCCESSFULLY')


        continue
    elif choice == 'b':
        print('PRINTING STUDENT RECORD')
        # print('student_record')

        for a, r in student_record.items():
            print(f'STUDENT ID - {a}, INFORMATION - {r}')
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        pass
        continue
    elif choice == 'e':
        pass
        continue
    elif choice == 'f':
        pass
        continue
    elif choice == 'g':
        print('SYSTEM EXIT')
        break
    else:
        print('INVALID CHOOICE, REENTER YOUR CHOICE')
        continue