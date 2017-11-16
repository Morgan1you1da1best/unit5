#Morgan Baughman
#11/16/17
#warmup13.py

from random import randint

numbers = []


for i in range(1,20):
    num = randint(1,1000)
    numbers.append(num)
    

numbers.sort()

print('The min is' , numbers[0])
print('The max is' , numbers[-1])
print('The sum is' , sum(numbers))