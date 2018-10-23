import numpy as np

def is_perfect_fast(n):
    if n == 1: return(False)
    sum = 1
    for zahl in range(2,int(np.sqrt(n))+1):
        if n%zahl == 0:
            sum += zahl + n/zahl
    return(sum == n)

def is_perfect_slow(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return(sum == n)
    
def perfect_numbers(n1, n2, method = 'slow'):
    """ prints all the perfect numbers in [n1,n2] (n1 < n2) in
        increasing fashion, using either a fast or a slow method
        (default method is 'slow')
    """
    if method == 'fast':
        fun = is_perfect_fast
    else:
        fun = is_perfect_slow

    for k in range(n1,n2+1):
        if fun(k) == True:
            print(k)

perfect_numbers(1,100000,method='fast')