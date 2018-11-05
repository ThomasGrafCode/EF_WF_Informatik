def wechselgeld(payments):
    five = ten = 0
    for pay in payments:
        if pay == 5:
            five += 1
        elif pay == 10:
            if not five:
                return(False)
            five -= 1
            ten += 1
        else:
            if five and ten:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return(False)
    return(True)

L = [5,5,10,10,20]
print(wechselgeld(L))