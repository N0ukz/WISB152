def priemzeef(N):
    #make a list of all the int up to and including N
    getallen = list(range(2, N))
    #make a loop that wil remove every integer not prime
    x = 0
    while x < N:
        if x in getallen:
            #check every number to see if its a multiple of x
            for y in range(x*2, N, x):
                if y in getallen:
                    getallen.remove(y)
        x += 1
    
    return getallen