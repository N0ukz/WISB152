class breuk:
    ''' rationaal getal waarop verschillende functies gedefinieerd zijn.
    teller is een geheel getal, noemer is een geheel getal ongelijk 0'''
    def __init__(self, teller = 0, noemer = 1):
        self._teller = teller
        self._noemer = noemer
        if noemer == 0:
            raise ZeroDivisionError("Je kunt helaas niet delen door nul")
        elif teller == 0:
            self._teller = 0
            self._noemer = 1
        else:
            if (teller < 0 and noemer >= 0) or (teller >= 0 and noemer < 0):
                teken = -1
            else:
                teken = 1
            (self._teller, self._noemer) = self._kleinst(teller, noemer, teken)
            
    def _kleinst(self, teller, noemer, teken):
        ''' zorgt dat de kleinst mogelijke breuk als antwoordt gegeven wordt '''
        a = abs(teller)
        b = abs(noemer)
        while a % b != 0:
            tempA = a
            tempB = b
            a = tempB
            b = tempA % tempB
        ret_t = abs(teller) // b * teken
        ret_n = abs(noemer) // b 
        return(ret_t, ret_n)    
    
    def Teller(self):
        return self._teller
    
    def Noemer(self):
        return self._noemer   
    
    def __str__(self): #Make it a string
        return str(self._teller) + '/' + str(self._noemer)
    
    def __float__(self): #make it a float
        return float(self._teller / self._noemer)
    
    def __int__(self): #make it an integer
        return int(self._teller / self._noemer)
    
    def __abs__(self): #return the absolute value
        return abs(self._teller / self._noemer)
    
    def __neg__(self):
        if (self._teller < 0 and self._noemer > 0) or (self._teller > 0 and self._noemer < 0):
            return breuk(self._teller, self._noemer)
        else:
            return breuk(-1*self._teller, self._noemer)
    
    def __pos__(self):
        if (self._teller < 0 and self._noemer > 0) or (self._teller > 0 and self._noemer < 0):
            return breuk(-1*self._teller, self._noemer)
        else:
            return breuk(self._teller, self._noemer)
    
    def __eq__(self, b): #check for equality
        a = self
        return (a.Noemer() == b.Noemer() and a.Teller() == b.Teller())
    
    def __ne__(self, b): #see if they're not equal to one another
        a = self
        return not a == b
    
    def __lt__(self, b): #see if left is smaller than right
        a = self
        return a.Teller() * b.Noemer() < a.Noemer() * b.Teller()
    
    def __le__(self, b): #see if right is bigger than left
        a = self
        return not b < a
    
    def __gt__(self, b): #reverse lt
        a = self
        return b < a
    
    def __ge__(self, b): #reverse le
        a = self
        return not b > a
    
    def __radd__(self, b): #define addition
        a = self
        if isinstance(b, breuk):
            teller = a.Teller() *  b.Noemer() + b.Teller() * a.Noemer()
            noemer = a.Noemer() * b.Noemer()
        elif isinstance(b, int):
            teller = a.Teller() + a.Noemer() * b
            noemer = a.Noemer()
        return breuk(teller, noemer)

    def __add__(self, b): #define addition
        a = self
        if isinstance(b, breuk):
            teller = a.Teller() *  b.Noemer() + b.Teller() * a.Noemer()
            noemer = a.Noemer() * b.Noemer()
        elif isinstance(b, int):
            teller = a.Teller() + a.Noemer() * b
            noemer = a.Noemer()
        return breuk(teller, noemer)
    

    def __rsub__(self, b): #define subtraction for different kind of numbers
        a = self
        if isinstance(b, breuk):
            teller = a.Teller() *  b.Noemer() - b.Teller() * a.Noemer()
            noemer = a.Noemer() * b.Noemer()
        elif isinstance(b, int):
            teller = a.Noemer() * b - a.Teller()
            noemer = a.Noemer()
        return breuk(teller, noemer) 

    def __sub__(self, b): #define subtraction for different kind of numbers
        a = self
        if isinstance(b, breuk):
            teller = a.Teller() *  b.Noemer() - b.Teller() * a.Noemer()
            noemer = a.Noemer() * b.Noemer()
        elif isinstance(b, int):
            teller = a.Teller() - a.Noemer() * b
            noemer = a.Noemer()
        return breuk(teller, noemer)

    def __rmul__(self, b):
        a = self 
        if isinstance(b, breuk):
            teller = a.Teller() * b.Teller()
            noemer = a.Noemer() * b.Noemer()
        elif isinstance(b, int):
            teller = a.Teller() * b
            noemer = a.Noemer()
        return breuk(teller, noemer)
    
    def __mul__(self, b):
        a = self 
        if isinstance(b, breuk):
            teller = a.Teller() * b.Teller()
            noemer = a.Noemer() * b.Noemer()
        elif isinstance(b, int):
            teller = a.Teller() * b
            noemer = a.Noemer()
        return breuk(teller, noemer)  
    
    def __rtruediv__(self, b): #reversed division
        a = self 
        if isinstance(b, breuk):
            teller = a.Teller() * b.Noemer()    
            noemer = a.Noemer() * b.Teller()
        elif isinstance(b, int):
            teller = a.Noemer() * b
            noemer = a.Teller() 
        return breuk(teller, noemer) 
    
    def __truediv__(self, b): #division for different inputs
        a = self 
        if isinstance(b, breuk):
            teller = a.Teller() * b.Noemer()    
            noemer = a.Noemer() * b.Teller()
        elif isinstance(b, int):
            teller = a.Teller()
            noemer = a.Noemer() * b
        return breuk(teller, noemer) 
    
    