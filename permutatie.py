class Permutatie:
    def __init__(self, inv):
        ''' Initial values for the list are given in tuples, which we will convert to lists in a list.
        We define the max, the empty list for the cyklictic answer and more. '''
        self.invoer = [list(map(int, x.lstrip('(').rstrip(')').split(','))) for x in str(inv).split(')(')]
        self.max_invoer = max(max(sublist) for sublist in self.invoer)
        self.elementen = list(range(1, self.max_invoer+1))
        self.aantal_cykels = len(self.invoer)
        self.cycle = []
        self.cycle_element = []
        self.cycle.append(Permutatie.cycle_een(self))
        self.cycle.append(Permutatie.cycle_verder(self))
        self.cycle[:] = (waarde for waarde in self.cycle if waarde != None)
        self.cycle[:] = (waarde for waarde in self.cycle if len(waarde) != 4)
        
    def cycle_een(self):
        ''' The first cycle will be started with 1; but can be any given value because the order of the cycles is not important. '''
        antwoord_lijst = []
        x = 1
        while x < self.max_invoer + 1:
            if x not in antwoord_lijst:
                antwoord_lijst.append(x)
                self.elementen.remove(x)
                x = Permutatie.functie(self.invoer, self.aantal_cykels - 1, x)
            else:
                self.cycle.append(str(tuple(antwoord_lijst)))
                break

    def cycle_verder(self):
        ''' The following cycles will be deteremined by this function '''
        antwoord_lijst = []
        for i in self.elementen:
            while i < self.max_invoer + 1:
                if i not in antwoord_lijst:
                    antwoord_lijst.append(i)
                    if i in self.elementen:
                        self.elementen.remove(i)
                    i = Permutatie.functie(self.invoer, self.aantal_cykels - 1, i)
                else:
                    self.cycle.append(str(tuple(antwoord_lijst)))
                    if self.elementen == []:
                        break
                    else:
                        return Permutatie.cycle_next(self)
    def __repr__(self):
        return (''.join(self.cycle)).replace(' ', '')
        
    def functie(invoer, index, a):
        ''' function that will find the next element in the cycle.
        a is the value of the element that you start with (from which we will assign the next value).
        It is a recussive function so that all cycles will be gone through.
        for example: [1,3,2] with a = 2, will return 1
        '''
        x = invoer[index]
        y = invoer[index - 1]
        if a in x:
            b = x.index(a)
            if b == len(x) - 1:
                c = x[0]
            else:
                c = x[b + 1]
            if c in y:
                d = y.index(c)
                if d == len(y) - 1:
                    e = y[0]
                else:
                    e = y[d + 1]
                if index > 1:
                    index -= 1
                    return Permutatie.functie(invoer, index, c)
                else:
                    return e
            else:
                if index > 1:
                    index -= 1  
                    return Permutatie.functie(invoer, index, c)
                else:
                    return c
        elif a in y:
            b = y.index(a)
            if b == len(y) - 1:
                c = y[0]
            else:
                c = y[b + 1]
            if index > 1:
                index -= 1
                return Permutatie.functie(invoer, index, a)
            else: 
                return c
        else:
            if index > 1:
                index -= 1
                return Permutatie.functie(invoer, index, a)
            else:
                return a

uitvoer = Permutatie(input())
print(uitvoer)
