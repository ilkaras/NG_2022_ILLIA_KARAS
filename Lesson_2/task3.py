a = int(input("Enter your number: "))
while a > 0:
    b = a
    while b > 0:
        print(b, end=" ")
        b = b - 1
    print(end="\n")
    a = a - 1