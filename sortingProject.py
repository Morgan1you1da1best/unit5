#Morgan Baughman
#11/27/17
#cocktailSort.py - implementation of cocktail sort

from random import randint
from time import time

N = 1000000 #how many numbers will be sorted

def quickSort(A,lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p - 1 )
        quicksort(A, p + 1, hi)
        
def partition(A, lo, hi):
    pivot = A[hi]
    i = lo -1
    for j in range(low,high):
        if A[j] < pivot:
            A[i], A[j] = A[j] , A[i]
    if A[ i ] > A[ i + 1 ]:
            A[hi], A[i+1] = A[i+1] , A[hi]
    return(i+1)
    
    """algorithm quicksort(A, lo, hi) is
    if lo < hi then
        p := partition(A, lo, hi)
        quicksort(A, lo, p - 1 )
        quicksort(A, p + 1, hi)

algorithm partition(A, lo, hi) is
    pivot := A[hi]
    i := lo - 1    
    for j := lo to hi - 1 do
        if A[j] < pivot then
            i := i + 1
            swap A[i] with A[j]
    if A[hi] < A[i + 1] then
        swap A[i + 1] with A[hi]
    return i + 1"""

if __name__ == '__main__':
    
    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
        
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = quickSort(numbers)
    t2 = time()
       
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
