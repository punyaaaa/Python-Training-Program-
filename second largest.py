# receiving 3 no as input
print("read 3 nos and check second largest number")
a = int(input("a enter num:"))
b = int(input("b enter num:"))
c = int(input("c enter num:"))

if (a >= b and a<= c) :
    print("a is second")
elif (b >=a and b <=c):
    print("b is second")
else:
    print("c is second")
