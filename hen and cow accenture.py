legs=int(input("enter the no of legs: "))
heads=int(input("enter the no of heads: "))
flag=False
for hen in range(heads):

    cow=heads-hen
    if (2*hen + 4*cow) == legs:
        print("Number of hens:", hen)
        print("Number of cows:", cow)
        flag=True
        break
if(not flag):
    print("No solution found")