def is_perfect(n):
    """ entscheidet, ob eine gegebene ganze Zahl n
        eine perfekte Zahl ist oder nicht
    """
    # eine perfekte Zahlen muessen groesser sein als 0:
    if n <= 0: 
        return(False)

    # summiere alle echten Teiler der Zahl n
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    # pruefe, ob die Summe der Teiler von n gerade
    # der Zahl n selbst entspricht (Definition einer
    # perfekten Zahl)
    return(sum == n)
    

def perfect_numbers(n1, n2):
    """ printet alle perfekten Zahlen in
        [n1,n2], mit n1 < n2, in aufsteigender
        Ordnung
    """
    for k in range(n1,n2+1):
        # pruefe fuer jede Zahl k in [n1,n2]
        # ob sie perfekt ist oder nicht
        # k wird ausgebeben <=> k ist perfekt
        if is_perfect(k) == True:
            print(k)

perfect_numbers(1,100000)