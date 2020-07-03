z,n,m = str.split(input())
z,n,m = float(z), int(n), int(m)
k = n
som = 0

#for k in range(n,m+1):
#    som = k * z ** k + som
#    k += 1
 
while k <= m:
    som = k * z ** k + som
    k += 1

print(format(som, ".2E"))