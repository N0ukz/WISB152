def lekkerofniet(x0,x1,x2):
    if x0 <= (0.5):
        y = 1
    else:
        if x1 <= (0.25):
            y = 2
        elif x1 >= (0.75):
            y = 2
        else:
            if x2 <= (0.3):
                y = 3
            elif (0.3) < x2 <= (0.6):
                y = 4
            else:
                y = 5
    return y