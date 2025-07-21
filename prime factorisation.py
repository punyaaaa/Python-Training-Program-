def primefact(n, i=2):
    for i in range(2,n+1):
        if n % i == 0:
            print(i, end=" ")
            primefact(n // i)
            break

n = int(input("Enter a number: "))
primefact(n)