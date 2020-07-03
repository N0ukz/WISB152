sudoku = [list(map(int, input().split())),
        list(map(int, input().split())),
        list(map(int, input().split())),
        list(map(int, input().split()))       
        ]

def oplossing(puzzel):
    #check eerst of er een lege plek is in de puzzel
    zoek = lege_plek(puzzel)
    if not zoek:
        return True
    else:
        rij, kolom = zoek
    
    for i in range(1, 5):
        if goedspel(puzzel, i, (rij, kolom)):
            puzzel[rij][kolom] = i
            if oplossing(puzzel):
                return True
            puzzel[rij][kolom] = 0
            
    return False

def goedspel(puzzel, getal, positie):
    #check de rij, controleer of er geen dubbele getallen zijn
    for i in range(len(puzzel[0])):
        if puzzel[positie[0]][i] == getal and positie[1] != i:
            return False
        
    #check de kolom, controleer of een getal niet voorkomt in een rij
    for i in range(len(puzzel)):
        if puzzel[i][positie[1]] == getal and positie[0] != i:
            return False
        
    #bepaal in welk vierkantje een element zit
    #geeft een element 0 of 1
    vierkant_x = positie[1] // 2
    vierkant_y = positie[0] // 2
    
    #check of een element voorkomt in het vierkantje
    #door twee keer te loopen over het vierkantje
    for i in range(vierkant_y * 2, vierkant_y * 2 + 2):
        for j in range(vierkant_x * 2, vierkant_x *2 + 2):
            if puzzel[i][j] == getal and (i,j) != positie:
                return False
    #als alles niet False is dan is het True
    return True

def printje(puzzel):
    '''Print de (opgeloste) sudokus in het juiste format'''
    for i in range(len(puzzel)):
        for j in range(len(puzzel[0])):
            if j == 3:
                print(puzzel[i][j])
            else:
                print(str(puzzel[i][j]) + ' ', end ="" )

                
def lege_plek(puzzel):
    ''' Zoek de plek met 0 in de puzzel en onthoud deze coordinaten'''
    for i in range(len(puzzel)):
        for j in range(len(puzzel[0])):
            if puzzel[i][j] == 0: # als de plek leeg is dan staat er een nul
                return (i, j) #rij, kolom
            
    #Als er niets gevonden wordt dan is hij leeg
    return None            

oplossing(sudoku)
printje(sudoku)

