adres = sorted(list(map(int, input().split())))

def calc_midden(adres):
    if len(adres) % 2 == 0:
        index = int(len(adres)/2)
        midden = (adres[index-1] + adres[index])/ 2
        return midden
    else:
        index = int(len(adres)//2)
        midden = adres[index]
        return midden
    
def som(adres, midden):
    som = 0
    for i in range(len(adres)):
        som = som + abs(adres[i] - midden)
    return print(int(som))

som(adres, calc_midden(adres))