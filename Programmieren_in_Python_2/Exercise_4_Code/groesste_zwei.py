def find_max(L):
    max = L[0]
    for element in L:
        if element > max:
            max = element
    return(max)

def find_largest_two(L):
    first_max = find_max(L)
    L.remove(first_max)
    second_max = find_max(L)
    return([first_max,second_max])

number = [-0.1,0.4,88,9,-100.2,88,0,2,2,3,5,2]
print(find_largest_two(number))
