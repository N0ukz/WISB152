#ask for the integers m, n, and split this at the space between them
m, n = map(int, input().split())

#define a function, which takes these inputs and uses them
def ackermann(m, n):
    #break the function into smaller pieces, so if m = 0, we print n +1
    if m == 0:
        return n + 1
    #if m != 0, but n = 0, we return the value of m - 1, and 1
    #however, we return the function, and will continue in the else statement
    #until both m and n are zero
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n-1))

print(ackermann(m, n))