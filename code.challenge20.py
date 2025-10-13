for lybag in range(1, 10, 1):
    for ly in range(9, lybag, -1):
        print(" ", end=" ")
    for bag in range(lybag, 0, -1):
        print(bag, end=" ")
    for leebug in range(2, lybag + 1,1):
        print(leebug, end=" ")
    print()
