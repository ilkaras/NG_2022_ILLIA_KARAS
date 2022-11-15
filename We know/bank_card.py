from rich.console import Console
console = Console()

def log(type, message):
    print ("[" + str(type) + "]: " + str(message))

def info(message):
    log ("INFO", message)

#==================================================================

numberList = []

def GetCardNumber():
    CardNumber = input("Enter credit card number: ")
    return CardNumber


def NumberListF(number):
    for elements in number:
        numberList.append(int(elements))


def DevideCardNumbersList():
    devidedList = [] 
    lenCardNumber = len(numberList) - 1
    while 0 < (lenCardNumber):          
        devidedList.append(numberList[lenCardNumber - 1 ]) 
        lenCardNumber = lenCardNumber - 2
    devidedList = (list(map(lambda x: x * 2, devidedList)))
    return devidedList 

def SortNumbers(number):
    for element in number:
        SortedNumbers = ''.join(str(element) for element in number)
    SortedNumbers = [int(num) for num in SortedNumbers]
    return SortedNumbers


def SumCardNumbersList():
    sumList = []
    lenCardNumber = len(numberList) - 1 
    while 0 < (lenCardNumber):
        sumList.append(numberList[lenCardNumber])
        lenCardNumber = lenCardNumber - 2
    return sumList

def SumNumbers(number, numbers):
    summa = sum(number) + sum(numbers)
    return summa
    
def Result(number):
    lenCardNumber = len(numberList) #16
    if number % 10 == 0:
        if lenCardNumber == 15 and (numberList[0:2] == [3,4] or numberList[0:2] == [3,7]):
            print("American Express")
        if lenCardNumber == 16 and (numberList[0:2] == [5,1] or numberList[0:2] == [5,2] or numberList[0:2] == [5,3] or numberList[0:2] == [5,4]):
                print("Master card")
        if (lenCardNumber == 16 or numberList == 13) and numberList[0] == [4]:
            print("Visa")
    else:
        print("INVALID card number")

def main():
    info("Program started")
    console.rule("[bold red] Menu")
    NumberListF(GetCardNumber())
    Result(SumNumbers(SortNumbers(DevideCardNumbersList()), SumCardNumbersList()))

main()