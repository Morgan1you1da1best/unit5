#Morgan Baughman
#11/30/17
#warpUp15.py - write a function that takes a list of numbers as an arguement and returns another list where each number is doubled.


def double(numbers):
    numdouble = []
    for num in numbers:
        num = (num*2)
        numdouble.append(num)
    return numdouble

print(double([2,4,6]))
    