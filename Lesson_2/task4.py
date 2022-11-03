print ("Program started, enter your number: ")
Number = int(input())
dobutok = 1
faktorial = 1
while dobutok < Number:
    faktorial += 1 
    dobutok = dobutok * faktorial         
print (str(Number)+ " = "+ str(faktorial) + "!")   