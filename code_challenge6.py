print("Welcome to THE ODD NUMBER SUMMATION")
num = 0
for lybag in range(1, 8, 1):
      c = eval(input("enter random number here ---->"))
      if c % 2 == 1:
          num += c
      
print("The summation of all add num is", num)
