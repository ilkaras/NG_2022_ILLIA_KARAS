alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
text = input("Input your text: ")
ChangeOrder = int(input("Enter change order: "))
transferedText = " "
for element in text:
    stockOrder = alphabet.find(element)
    NewText = stockOrder + ChangeOrder
    if element in alphabet:
        transferedText += alphabet[NewText]
    else:
        transferedText += element
print("Translated text: " + "\n" + str(transferedText))