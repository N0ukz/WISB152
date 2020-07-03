def roman2int(n):
    swap = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
    som = 0
    for i in range(len(n)):
        waarde = swap[n[i]]
        if i+1 < len(n) and swap[n[i+1]] > waarde:
            som -= waarde
        else:
            som += waarde
    return som

def int2roman(o):
    getal=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romein = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    swap = []
    for i in range(len(getal)):
        geheelgetal = o // getal[i]
        swap.append(geheelgetal * romein[i])
        o = o - geheelgetal * getal[i]
        romeins = "".join(map(str, swap))
        
    return romeins
    

def roman2int2(n):
    #make a list of all the char in input, all strings
    char = list(map(str, n))
    som = []
    x = 0

    #assign a numerical value to every "letter"
    for x in range(0, len(char)+1):
         if char[x] == str("M"):
             char[x] = 1000
         elif char[x] == str('D'):
             char[x] = 500
         elif char[x] == str('C'):
             char[x] = 100
         elif char[x] == str("L"):
             char[x] = 50
         elif char[x] == str("X"):
             char[x] = 10
         elif char[x] == str("V"):
             char[x] = 5
         elif char[x] == str("I"):
             char[x] = 1
    
    k = 1
    a = 0
    b = 0
    c = 0
    
    while k in range(1, len(char)+1):
        if k < len(char):
            if char[k] > char[k-1]:
                k = k-1
                a = char[k+1]-char[k]
                som.append(a)
                k += 3
                if k > len(char)+1:
                    break
            elif char[k] <= char[k-1]:
                k = k-1
                b = char[k]
                som.append(b)
                k += 2
                if k > len(char)+1:
                    break
        elif k == len(char):
            k = k-1
            c = char[k]
            som.append(c)
            break
    
    return sum(som)

def int2roman2(x):
    lijst = []
    char = list(map(int, x))
    if len(char) == 4:
        a = char[0] * 1000
        lijst.append(a)
        b = char[1] * 100
        lijst.append(b)
        c = char[2] * 10
        lijst.append(c)
        d = char[3]
        lijst.append(d)
    elif len(char) == 3:
        a = 0
        lijst.append(a)
        b = char[0] * 100
        lijst.append(b)
        c = char[1] * 10
        lijst.append(c)
        d = char[2]
        lijst.append(d)
    elif len(char) == 2:
        a = 0
        lijst.append(a)
        b = 0
        lijst.append(b)
        c = char[0] * 10
        lijst.append(c)
        d = char[1]
        lijst.append(d)
    elif len(char) == 1:
        a = 0
        lijst.append(a)
        b = 0
        lijst.append(b)
        c = 0
        lijst.append(c)
        d = char[0]
        lijst.append(d)
    
    lijstR = []
    
    if lijst[a] != 0:
        lijstR.append(a*"M")
    elif lijst[b] == 9:
        lijstR.append("CM")
    elif lijst[b] >= 5:
        lijstR.append("D")
        lijstR.append((b-5)*"C")
    elif lijst[b] == 4:
        lijstR.append("CD")
    elif lijst[b] <4:
        lijstR.append(b*"C")
    elif lijst[c] == 9:
        lijstR.append("XC")
    elif lijst[c] >= 5:
        lijstR.append("L")
        lijstR.append((c-5)*"X")
    elif lijst[c] == 4:
        lijstR.append("XL")
    elif lijst[c] <4:
        lijstR.append(c*"L")
    elif lijst[d] == 9:
        lijstR.append("IX")
    elif lijst[d] >= 5:
        lijstR.append("V")
        lijstR.append((d-5)*"I")
    elif lijst[d] == 4:
        lijstR.append("IV")
    elif lijst[d] <4:
        lijstR.append(d*"I")
        
    Rom = "".join(map(str, lijstR))
    
    return Rom
