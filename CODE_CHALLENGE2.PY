money = eval(input("Enter the amount to deposit:"))
print("Here's the amount of ")

a1 = money // 1000
m1 = money % 1000

a2 = m1 // 500
m2 = m1 % 500

a3 = m2 // 200
m3 = m2 % 200

a4 = m3 // 100
m4 = m3 % 100

a5 = m4 // 50
m5 = m4 % 50

a6 = m5 // 20
m6 = m5 % 20

a7 = m6 // 10
m7 = m6 % 10

a8 = m7 // 5
m8 = m7 % 5

a9 = m8 // 1
m9 = m8 % 1

print("Here is your breakdown to your deposit", money)
print(a1 ,"-1000")
print(a2 ,"-500")
print(a3 ,"-200")
print(a4 ,"-100")
print(a5 ,"-50")
print(a6 ,"-20")
print(a7 ,"-10")
print(a8 ,"-5")
print(a9 ,"-1")