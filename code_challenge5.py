num = eval(input("enter a number here ---> "))
result = 1
for lybag in range(num, 0, -1):
    result *= lybag
print("the factorial of",num, "is",result)
