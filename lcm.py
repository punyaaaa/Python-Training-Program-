a = int(input("a = "))
b = int(input("b = (a enter the no :)"))
if a > b:
    big = a
else:
    big = b
step = big
while True:
    if big % a == 0 and big % b == 0:
        print("a lcm is =", big)
        break
    else:
        big = big + step
