'''Vraag welk jaar we moeten checken op schrikkelbaarheid''' 
jaar = input()
jaar = int(jaar) # make sure the value is seen as an int

if jaar % 4 == 0 and not jaar % 100 == 0: #als het jaar deelbaar is door 4, maar niet door 100 dan is het een schrikkeljaar
    print("schrikkeljaar")
elif jaar % 400 == 0: #Echter als het deelbaar is door 400, dan wel
    print("schrikkeljaar")
else: #wanneer niet deelbaar door 4, 100 of 400, dan is het geen schrikkeljaar.
    print("geen schrikkeljaar")