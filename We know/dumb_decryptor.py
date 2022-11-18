alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
text = input("Input your text: ")
ChangeOrder = 25
while ChangeOrder > 0: 
    transferedText = " "
    for element in text:
        stockOrder = alphabet.find(element)
        NewText = stockOrder + ChangeOrder
        if element in alphabet:
            transferedText += alphabet[NewText]
        else:
            transferedText += element
    print("Rot" + str(ChangeOrder) +  "\n" + str(transferedText))
    ChangeOrder = ChangeOrder - 1

    