
# table = eval(input("Enter Number of Table: "))

# for lybag in range(1, 13, 1):
#     for x in range(1, table + 1, 1):
#         print(f"{x} x {lybag} = {x*lybag}", end="\t")
#     print()


for lybag in range(1,6,1):
    for x in range(6, lybag, -1):
        print(" ",end=" ")
    for y in range(1,lybag + 1,1):
        print(" * ",end=" ")
    print()