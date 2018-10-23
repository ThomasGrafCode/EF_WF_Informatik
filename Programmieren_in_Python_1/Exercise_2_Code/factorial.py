def factorial(n):
    """ berechnet n! (n-Fakultaet) fuer gegebenes n
    """
    fak = 1
    for k in range(2,n+1):
        fak = fak * k
    return(fak)