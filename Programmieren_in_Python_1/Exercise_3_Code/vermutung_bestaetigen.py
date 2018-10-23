def check_assumption(n):
    for i in range(2,n+1):
        if (n**3 - n) % 3 != 0:
            print('Die Behauptung ist zumindest fuer n =',i,'falsch')
            return(False)
    print('Die Behauptung stimmt zumindest bis n =',n)
    return(True)