def find_max(L):
    max = L[0]
    for element in L:
        if element > max:
            max = element
    return(max)

number = [-0.1,0.4,9,-100.2,88,0,2]
print(find_max(number))
