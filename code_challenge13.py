r = input('enter your name here --> ')

print('##################################################')
print(' welcome to our ODD NUMBER SUMMATION', r)
print(' ODD NUMBER SUMMATION, PRESS 0 TO STOP ')
print('##################################################\n')

d = True
sum = 0
odd = ''

while d == True:
    num = eval(input('input random number here >>>> '))

    if num %2 == 1:
        print('---ODD NUMBER DETECTED, CODE CONTINUES--- ')
        sum += num 
        odd += str(num) + ' '
        continue
    elif num == 0:
        print('<PROGRAM STOP!!!>')
        break
    else:
        if num %2 == 0:
            print('---EVEN NUMBER DETECTED!, CODE CONTINUES--- ')         
        else:
            print('<invalid output>')
        continue
print(f'Hi {r}, the sum of all ODD number is {sum}')
print(f'ODD numbers detected included the ff {odd}')
