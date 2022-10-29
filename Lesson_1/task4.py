a = int(input("Type a: "))
b = int(input("Type b: "))
c = int(input("Type c: "))
D = float(b * b - 4 * a * c)
if D > 0 :
    print ("x1= " + str(( -b + (D ** 0.5)) / (2 * a)))
    print ("x2= " + str(( -b - (D ** 0.5)) / (2 * a)), end="")
if D == 0 :
    print ("x= " + str(-b / (2 * a)), end="")
if D < 0 :
    print ("There is no solution", end="")