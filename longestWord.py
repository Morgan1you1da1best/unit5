#Morgan Baughman
#11/15/17
#longestWord.py - pirnt out the longest word

words = input('Enter a list of words: ').split(' ')

word = ""
w = 1

for w in words:
    length = len(w)
    if length > len(word):
        word = w
    
print(word)
        

