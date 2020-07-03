#repeat a step such that eventually the element are equal
def bisectie_it(lijst, doel):
    #vergelijk het laatste element en het eerste element met a
    x = 0
    y = len(lijst)-1
    #check if doel is an element in the lijst
    z = lijst.count(doel)
    if z > 0:
        while x < y:
            #if doel is in the list we use the method given in the excersise
            a = int((x+y)//2)
            if lijst[a] < doel:
                x = a + 1
            else:
                y = a
        return x
    #if the element is not in the lijst we return -1
    else:
        return -1   

def bisectie_rec(lijst, doel):
    #check if an element x from 0 to end of the list is equal to the doel
    for x in range(len(lijst)):
        if doel == lijst[x]:
            #if so return x
            return x
    else:
        #if not, return -1
        return -1
