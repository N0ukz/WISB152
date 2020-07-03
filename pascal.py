#pascals triangle
k,n = input().split() # n amount of rows, k place in row
k,n = int(k),int(n)
def pascal(n,k):
    #create a 2D list with 0 we will assign correct numbers in the next step
    driehoek = [[0 for x in range(n)]for y in range(n)] 
    #fill the row
    for row in range(n):
        #some place i in range
        for i in range(row+1):
            if i == 0 or i == row:
                driehoek[row][i] = 1
            else:
                driehoek[row][i] = driehoek[row-1][i-1] + driehoek[row-1][i]
    return driehoek[n-1][k-1]
print(pascal(n,k))
