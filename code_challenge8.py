num = eval(input("enter number for multiplication table ---> "))

for lybag in range(1, 13, 1):
    result = num * lybag
    print(num, "x", lybag, "=", result)
