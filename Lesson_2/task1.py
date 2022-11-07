print ("======================")
sentence = input("Write your sentence: ")
print ("======================")
sentence = sentence.replace(" ","")

AmmountOfLetters = len(sentence)
CountedLetters = {element: sentence.count(element) for element in set(sentence)}
SortedLetters = dict(sorted(CountedLetters.items(), key=lambda item: item[0]))

print (" Ammount of letters in your sentense: " + str(AmmountOfLetters)
 +"\n","How many letters different types in your sentence: " + str(CountedLetters)
 +"\n" + " Sorted letters: " + str(SortedLetters))