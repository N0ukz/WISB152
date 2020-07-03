invoer1 = list(map(int, input().split()))
invoer2 = list(map(int, input().split()))
opgaven = []
wiskund = []

#create a list from high to low of both the exc and mathlvl
for x in range(len(invoer1)):
    a = max(invoer1)
    opgaven.append(a)
    invoer1.remove(a)
    b = max(invoer2)
    wiskund.append(b)
    invoer2.remove(b)
    
laag = 0
hoog = len(invoer) - 1
    
def sorteer(invoer, laag, hoog):
    i = laag - 1
    pivot = invoer[hoog]
    
    for j in range(laag, hoog):
        if invoer[j] < pivot:
            i += 1
            invoer[i], invoer[j] = invoer[j], invoer[i]
    invoer[i+1], invoer[hoog] = invoer[hoog], invoer[i+j]
    return (i+1)

def quickSort(invoer, laag, hoog):
    if laag < hoog:    
        pi = sorteer(invoer, laag, hoog)
        quickSort(invoer, laag, pi-1)
        quickSort(invoer, pi+1, hoog)



#if the mathlvl is at least two times higher than the exc
#they can do the exc and will thus be rmvd from the lists
#if not its impossible
while x in range(len(wiskund)):
    if wiskund[x] >= opgaven[x] and not 2*opgaven[x] < wiskund[x] :
        m = 1
        wiskund.remove(wiskund[x])
        opgaven.remove(opgaven[x])
        x+= 1
    else:
        m = 0
        break

if m == 1:
    print("mogelijk")
elif m == 0:
    print("onmogelijk")
