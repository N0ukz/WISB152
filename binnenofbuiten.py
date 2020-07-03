# Check of je koeien binnen of buiten staan!
locatie = input('Wat zijn de coordinaten van de Koe? ')
x, y = locatie.split(",")
x_koe = float(x)
y_koe = float(y)

x1_veld = 52 + 4/60 + 52/3600
y1_veld = 5 + 9/60 + 49/3600
x2_veld = 52 + 5/60 + 28/3600
y2_veld = 5 + 11/60 + 5/3600

if x1_veld <= x_koe <= x2_veld and y1_veld <= y_koe <= y2_veld:
    print('binnen')
else:
    print('buiten')
        