print ("======================")
sentence = input("Write your sentence: ")
print ("======================")
sentence = sentence.replace(" ","")

AmmountOfLetters = len(sentence)
CountedLetters = {i: sentence.count(i) for i in set(sentence)}
SortedLetters = sorted(CountedLetters.keys())

print (" Ammount of letters in your sentense: " + str(AmmountOfLetters)
 +"\n","How many letters different types in your sentence: " + str(CountedLetters)
 +"\n" + " Sorted letters: " + str(SortedLetters))