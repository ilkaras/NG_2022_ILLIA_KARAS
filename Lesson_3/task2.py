def log(type, message):
    print ("[" + str(type) + "]: " + str(message))

def info(message):
    log ("INFO", message)

def AskString(message):
    return input(message)

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
        Text = Text.split(" ")
        Text.sort()
        return Text
    elif number == 2:
        Text = len(Text)
        return Text
    elif number == 3:
        VariatnOfLetters = int(input("consonants [1] or vowels [2] ? : "))
        if VariatnOfLetters == 1:
            lst = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']
            for element in lst:
                while element in Text:
                    Text = Text.replace(element, '')
        elif VariatnOfLetters == 2:
            lst = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P',
             'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z','b', 'c', 'd', 'f', 'g', 'h',
              'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
            for element in lst:
                while element in Text:
                    Text = Text.replace(element, '')
        return Text
    elif number == 4:
        TextList = Text.split()
        TextList.reverse()
        return TextList
    elif number == 5:
        TextList = Text.split()
        WordNumber = int(input("Enter number of word: "))
        NumberedWord = TextList[WordNumber - 1]
        return NumberedWord
    elif number == 6:
        return Text
    elif number == 7:
        Exit = "!!!Program closed!!!"
        return Exit


def main():
    info("Program started")
    Text = AskString("Write your text: ")
    Actions()
    Result = Sample(Choise(), Text)
    info("Result: " + str(Result))

main()