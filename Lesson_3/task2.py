def log(type, message):
    print ("[" + str(type) + "]: " + str(message))

def info(message):
    log ("INFO", message)

def AskString(message):
    return input(message).split(" ")

def Actions():
    print("[1] Sort string")
    print("[2] Count the number of elements")
    print("[3] Print vowels or consonants")
    print("[4] Break by words, and remove words from the end")
    print("[5] Print word by number")
    print("[6] Write the line again")
    print("[7] Exit from the program")

def Choise():
    return int(input("Enter your variant: "))

def Sample(number, Text):
    if number == 1:
        Text.sort()
        return Text
    elif number == 2:
        SecondFunktion()

def main():
    info("Program started")
    Text = AskString("Write your text: ")
    Actions()
    Result = Sample(Choise(), Text)
    info("Result: " + str(Result))

main()