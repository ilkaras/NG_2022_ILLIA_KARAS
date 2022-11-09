sentence = input("Write your sentence: ")
CountedElements = {i: sentence.count(i) for i in set(sentence)}
print("Elements and ammount: " + str(CountedElements))