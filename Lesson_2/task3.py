First_number = int(input("Enter your number: "))
while First_number > 0:
    Other_numbers = First_number
    while Other_numbers > 0:
        print(Other_numbers, end=" ")
        Other_numbers = Other_numbers - 1
    print(end="\n")
    First_number = First_number - 1