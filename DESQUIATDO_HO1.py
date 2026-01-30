lybag = input('ENTER YOUR WORD HERE --> ')
ly = len(lybag)
bee = []
for bag in range(1, ly + 1, 1):
    lee = int(input(f'ENTER NUMBER {bag}: '))
    bee.append(lee)
print(bee)
print(f'THE LENGTH OF THE WORD IS {ly} ')
total = 0
for num in bee:
    total = total + num
ave = total/ly
print(f"THE AVERAGE OF THE NUMBER IS {ave} ")
if ave < bee:
    print(f"THE LENGTH OF THE WORD '{lybag}' LESS THAN THE AVERAGE. ")
elif ave > bee:
    print(f"THE LENGTH OF THE WORD '{lybag}' IS LESS THAN THE AVERAGE. ")
elif ave == bee:
    print(f"THE LENGTH OF THE WORD '{lybag}' IS EQUAL THAN THE AVERAGE. ")
    