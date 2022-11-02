def log(type, message):
    print ("["+ str(type) + "] : " + str(message))

def info(message):
    log ("INFO", message)


def AskNumber(message):
        return float(input(message))

def MathCase(FirstNumber, SecondNumber,MathWay):
    match MathWay:
        case 'plus':
            return FirstNumber + SecondNumber
        case 'minus':
            return FirstNumber - SecondNumber
        case 'multiply':
            return FirstNumber * SecondNumber
        case 'devide':
            return FirstNumber / SecondNumber
        case 'pod koren':
            return FirstNumber ** 0.5, SecondNumber ** 0.5
        
        case 'v stepen':
            return FirstNumber * FirstNumber, SecondNumber * SecondNumber
        

def AskMathWay(message):
    return input(message)

def main():
    info ("Program started")
    FirstNumber = AskNumber("Enter first value: ")
    SecondNumber = AskNumber("Enter second value: ")
    MathWay = AskMathWay("Choose what Math case: (plus,minus,multiply,devide,v stepen, pod koren): ")
    MathCase (FirstNumber, SecondNumber, MathWay)
    info ("Variable initialized")
    info ("Result: " + str(MathCase(FirstNumber, SecondNumber, MathWay)))
main()













