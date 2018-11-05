def ist_monoton(L):
    monoton_steigend = True
    monoton_fallend = True
    
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            monoton_steigend = False
        if L[i] < L[i+1]:
            monoton_fallend = False
    
    return(monoton_steigend or monoton_fallend)

# man kann das 'all' keyword verwenden, um den Code
# noch kompakter zu machen
def ist_monoton_kompakt(L):
    index = len(L) - 1 
    return (all(L[i] <= L[i+1] for i in range(index)) or 
                all(L[i] >= L[i+1] for i in range(index)))

L = [1,1,1,1,1,1,1,1,1]