a = int(input("enter the number:"))
b = int(input("enter the number:"))
c=0
while(b!=0):
    c = a % b
    a = b
    b = c
print("gcd=", a)
