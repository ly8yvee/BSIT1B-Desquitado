import os
import json

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
        os.system('cls')

        print('SEARCH STUDENT RECORD')

        search_id = input('input Student ID for search ---> ').lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("=========================================")
                print('RECORD FOUND for ID {search_id}')
                # to print the student for the serached ID
                for a in student_record[search_id]:
                    print(f' --- {a}')
                print("=========================================")
            else:
                print('\n\nNO RECORD FOUND')
            break
        continue
    elif choice == 'd':
        os.system('cls')

        print('DELETE STUDENT RECORD')

        search_id = input('input Student ID for search ---> ').lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("=========================================")
                print('RECORD FOUND for ID {search_id} ')
                # to print the student for the serached ID
                for a in student_record[search_id]:
                    print(f' --- {a}')
                print("=========================================")
                # .pop() to delete an item
                student_record.pop(search_id)
            else:
                print('\n\nNO RECORD FOUND')
            break
        continue
    elif choice == 'e':
        os.system('cls')

        print('EDIT/MODIFY STUDENT RECORD')

        search_id = input('input Student ID for search ---> ').lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("=========================================")
                print('RECORD FOUND for ID {search_id}')
                # to print the student for the serached ID
                for a in student_record[search_id]:
                    print(f' --- {a}')
                print("=========================================")
                #new set of value for serach id
                first_name = input('pleaase input Styudent First Name ---> ').upper()
                second_name = input('please input Student Second Name ---> ').upper()
                age = eval(input('input student age ---> '))
                course = input('input student course ---> ').upper()
                section = input('input student section ---> ').upper()

                student_record[search_id][0] = first_name
                student_record[search_id][1] = second_name
                student_record[search_id][2] = age
                student_record[search_id][3] = course
                student_record[search_id][4] = section

                print('updated')

            else:
                print('\n\nNO RECORD FOUND')
            break

        continue
    elif choice == 'f':
        print('EXPORT STUIDENT DATA')
        #JSON JAVASCRIPT OBJECT NOTATION

        with open('student_record.json', 'w') as new_file:
            json.dump(student_record,new_file, indent=4)

        print('\n\nDATA EXPORTED TO JSON')
        
        continue
    elif choice == 'g':
        print('SYSTEM EXIT')
        break
    else:
        print('INVALID CHOOICE, REENTER YOUR CHOICE')
        continue
