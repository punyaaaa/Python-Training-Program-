sum = 0
while True:
    a = int(input("a enter marks:"))
    if a == 0:
        break
    if a <= 100:
        sum += a
print("sum is =", sum)
