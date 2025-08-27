name = input("what is your is your name? ---> ")
fare = eval(input("fare fee? ---> "))
isStudent = input("are you currently a student (yes / no) ")

if isStudent == 'yes' :
    discount = fare * 0.2
    #fare -= discount
    new_fare = fare - discount
    print("Hi ", name, "yor discount is ", discount)
    print("your new fare is ", new_fare)

else: 
    print("Sorry " , name,  "You are not eligible for a student discount")
    
