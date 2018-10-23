def is_perfect_slow(n):
    """ decides if a given integer n is a perfect number or not
        this is the straightforward implementation
    """
    if n <= 0:
        return(False)
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return(sum == n)


def is_perfect_fast(n):
    """ decides if a given integer n is a perfect number or not
        this is a slightly less naive implementation which relies on
        the following mathematical fact:
        suppose n is a positive integer such that n = pq, with p, q prime
        then either p <= sqrt(n) or q <= sqrt(n)
    """
    if n <= 0:
        return(False)
    sum = 0
    i = 1
    cond = 1
    while cond <= n:
        if n % i == 0:
            sum += i
            if cond != n:
                sum += float(n/i)
        i += 1
        cond = i**2
    return(sum - n == n)


def perfect_numbers(n1, n2, method = 'fast'):
    """ prints all the perfect numbers in [n1,n2] (n1 < n2) in
        increasing fashion, using either a fast or a slow method
        (default method is 'fast')
    """
    if method == 'fast':
        fun = is_perfect_fast
    else:
        fun = is_perfect_slow

    for k in range(n1,n2+1):
        if fun(k) == True:
            print(k)
