#Morgan Baughman
#11/13/17
#listDemo.py -print out first and last words in a list

words = input('Enter some words').split(' ')

#print out the list one item per line
for w in words:
    print(w)
    
print('The first word was', words[0])
print('The last word was', words[-1])


