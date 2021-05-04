import string,re

with open('book1.txt', 'r') as file:
    book1 = file.read().replace('\n', '')

with open('book2.txt', 'r') as file:
    book2 = file.read().replace('\n', '')

#Putting all words in lower case
book1 = book1.lower()
book2 = book2.lower()    
    
#Removing punctuation marks 
book1Final = book1.translate(str.maketrans('', '', string.punctuation+'“”'))
book2Final = book2.translate(str.maketrans('', '', string.punctuation+'“”'))

#Removing extra spaces between words
book1Final = re.sub(' +', ' ', book1Final)
book2Final = re.sub(' +', ' ', book2Final)

book1Words = set(book1Final.split())
book2Words = set(book2Final.split())

commonWords = book1Words.intersection(book2Words)

print(commonWords)
print(len(commonWords))
