import random

print('*****************************')
print('******* GUESSING GAME *******')
print('*****************************\n')

random_value = random.randint(1,10)
tries = 0
tuloy = True

while tuloy == True:
    r = eval(input(' guess a random number from 0 to 20 ---> '))

    tries += 1
    if r == random_value:
       print('YEHEYY!!! WINNER KA PO BABY!!!')
       print(f'random value is {random_value}')
       break
    else:
        print('WRONG KA PO BABY, ULITIN MO PO >.<')
    continue
print(f'you guessed {tries} times')

