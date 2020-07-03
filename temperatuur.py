#vergelijk een aantal getallen met elkaar, grootste verschil dag weergeven
z = input()
lijst = list(map(int, z.split()))
def temp(lijst):
    #create elements that you can compare
    a = lijst[len(lijst)-1] #last element in list
    aa = len(lijst)-1 #assign its place
    b = lijst[0] #first elemnt in list
    bb = 0 #assign its place
    for x in range(1, len(lijst)):
        #if the value of the list is smaller than a and its place is bigger then b
        #we change the value of a to this new place x
        if lijst[(len(lijst) - x)] < a and bb < x:
            a = lijst[len(lijst)-x]
            aa = len(lijst)-x
        #if the value is bigger than b but the place smaller than a
        #we change the value of b
        elif lijst[x] > b and x < aa-1:
            b = lijst[x]
            bb = x
    #when the difference is the most; we print this
    if bb < aa:
        c = b-a
        return c
    #however if theres no such thing as difference, we return 0
    elif b==a:
        c = 0
        return c
print(temp(lijst))