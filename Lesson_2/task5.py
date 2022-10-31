Entered_list = input("Enter your list: ").split(", ")
ints = []
for elements in Entered_list:
    ints.append(int(elements))
ints.sort()
ostatok = ints[1:-1]
sum = 0
for num in ostatok:
    sum = sum + int(num)
print ("First element: " + str(ints[0]) + "\nLast element: " + str(ints[-1]) + "\nSum: " + str(sum))
