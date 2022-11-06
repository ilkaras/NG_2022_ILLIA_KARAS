alphabet = "zyxwvutsrqponmlkjihgfedcba"
numbeOfChange = int(input("Change order: "))
Text = input("Write your text: ")
change = str.maketrans(alphabet, alphabet[numbeOfChange:]+alphabet[:numbeOfChange])
translation = Text.translate(change)
print('Result: "' + translation + '"') # Result: "lcdpcfdhvdu"