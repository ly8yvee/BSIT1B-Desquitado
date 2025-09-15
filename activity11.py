temp = eval(input("enter temperature ---> "))

if temp.isnumeric():
        if temp <= 0: 
                print("below freezing")
        elif temp >= 16 and temp <= 30:
                print("cold temperature")
        elif temp >= 1 and temp <= 15:
                print("extremely cold")
        elif temp >= 31 and <= 38:
                print("lukewarm")
        elif temp >= 39 and <= 42:
                print("warm") 
        elif temp >= 43 and <= 50:
                print("hot")
        elif temp >= 51 and <= 60:
                print("extremely hot")
        elif temp >= 61:
        
        else:
                print("burning")    

else:
        print("invalid temperature")    
        