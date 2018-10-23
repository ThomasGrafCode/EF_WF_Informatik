def power_8(a):
    """ berechnet a^8 fuer gegebenes a
    """
    # einfache Anwendung des Potenzgesetzes:
    # a^b * a^c = a^(b+c) 
    b = a*a # b == a^2 (erste Multiplikation)
    c = b*b # c == a^4 (zweite Multiplikation)
    d = c*c # d == a^8 (dritte Multiplikation)
    return(d)