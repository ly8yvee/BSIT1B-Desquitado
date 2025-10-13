print("\t\t A",end=" ")
for lybag in range(1,11,1):
    for ly in range(10, lybag, -1):
        print(" ", end=" ")
    for bag in range(1, lybag, 1):
        print("*", end=" ")
    for leebug in range(1, lybag, 1):
        print("*", end=" ")
    print()
