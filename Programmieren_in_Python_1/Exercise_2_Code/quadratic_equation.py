from numpy import sqrt # importiere die Wurzel-Funktion

def solve_quadratic_equation(a, b, c):
    """ berechnet (falls sie exisiteren)
        die Loesungen / Loesung der quadratischen Gleichung
        ax^2 + bx + c = 0
        fuer beliebige reelle Zahlen a, b, c
    """
    
    # quadratischer Fall (quadratische Gleichung)
    if a != 0:
        # berechne die Diskriminante
        D = b**2. - 4.*a*c
        
        # keine reellen Loesungen fuer D < 0
        # (Wurzel einer negativen Zahl)
        if D < 0:
            print('negative Diskriminantne D =',D,'\n')
            print('keine reellen Loesungen')
            return
        # Mitternachtformel
        # es gibt zwei verschiedene Loesungen fuer D != 0
        # und genau eine (doppelte) Loesung fuer D == 0
        else:
            wd = sqrt(D) # wd = Wurzel der Diskriminante
            x1 = (-b + wd)/(2.*a) # Mitternachtsformel
            x2 = (-b - wd)/(2.*a) # Mitternachtsformel
            return([x1, x2])

    # linearer Fall (lineare Gleichung)
    elif b != 0:
        x = -c/float(b) # Loesung einer linearen Gleichung
        return(x)
    
    # konstanter Fall
    elif c != 0:
        print('Fall c = 0, mit c ==',c,':\n')
        print('diese Gleichung ist nie erfuellt')
        return
    else:
        print('Fall c = 0, mit c ==',c,':\n')
        print('diese Gleichung ist trivialerweise erfuellt')
        return


solutions = solve_quadratic_equation(3,-4,-15) # Beispiel