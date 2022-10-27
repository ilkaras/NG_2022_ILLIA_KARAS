FirstNumber = float(input("Enter first number: "))
SecondNumber = float(input("Enter second number: "))
MathWay = input("Choose what i need to do(plus,minus,multiply,devide,v stepen,pod koren): ")
if MathWay == "plus" :
   print ("Sum: " + str(FirstNumber + SecondNumber), end="")
if MathWay == "minus" :
    print ("Vidnimannia : " + str(FirstNumber - SecondNumber), end="")
if MathWay == "multiply" :
    print ("Dobytok :" + str(FirstNumber * SecondNumber), end="")
if MathWay == "devide" :
    print ("Riznitsia: " + str(FirstNumber / SecondNumber), end="")
if MathWay == "v stepen" :
    print ("stepen first number :" + str(FirstNumber * FirstNumber))
    print ("stepen second number :" + str(SecondNumber * SecondNumber), end="")
if MathWay == "pod koren" :
    print ("koren first number: " + str(FirstNumber ** 0.5))
    print ("koren second number: " + str(SecondNumber ** 0.5), end="")
    