alphabet = ["abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
alphabetForDec = (alphabet[0]*2, alphabet[1]*2)
text = input("Input your text: ")
Rot = len(alphabet[0])
while Rot > 0: 
    transferedText = ""
    for element in text:  
        if element in alphabetForDec[0]:
            stockOrder = alphabetForDec[0].find(element)
            NewText = stockOrder + Rot
            transferedText += alphabetForDec[0][NewText]
        elif element in alphabetForDec[1]:
            stockOrder = alphabetForDec[1].find(element)
            NewText = stockOrder + Rot
            transferedText += alphabetForDec[1][NewText]
        else:
            transferedText += element
    print("Rot" + str(Rot) +  "\n" + str(transferedText))
    Rot = Rot - 1

    