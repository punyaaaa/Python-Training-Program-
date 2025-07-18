def sq(x):
    return x * x    
def rectangle(l, b):
    return l * b
def circle(r):
    return 3.14 * r * r
def triangle(b, h):
    return 0.5 * b * h

while True:
    print("1: square")
    print("2: rectangle")
    print("3: circle")
    print("4: triangle")
    print("5.exit")
    ch = int(input("Enter your choice:"))
    match ch:
        case 1:
            x = int(input("side:"))
            print(sq(x))
        case 2:
            l = int(input("length:"))
            b = int(input("breadth:"))
            print(rectangle(l,b))
        case 3:
            r = int(input("radius:"))
            print(circle(r))
        case 4:
            b = int(input("base:"))
            h = int(input("height:"))
            print(triangle(b,h))
        case 5:
            exit(0)
        case _:
            print("done")

