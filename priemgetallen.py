def priemzeef(n):
    #make a list of all true values from place zero up to place n
    lijst = [True] * (n+1)
    #values 0 and 1 are not prime
    lijst[0] = lijst[1] = False
    
    p = 2
    
    while (p**2 <= n):
        if lijst[p] == True:
            #if p is a multiple of itself in the list, while take stepsizes p
            #p is not prime
            for i in range(p*2, n+1, p):
                lijst[i] = False
        p += 1
    
    priem = []
    # add the VALUE of p to a new list
    for p in range(n+1):
        if lijst[p]:
            priem.append(p)
    
    return priem
    
    
# =============================================================================
# priemzeef_cache = {}
# def priemzeef1(N):
#      if N in priemzeef_cache:
#          return priemzeef_cache[N]
#     
#      #make a list of all the int up to and including N
#      getallen = list(range(2, N))
#      #make a loop that wil remove every integer not prime
#      x = 0
#      while x < N:
#          if x in getallen:
#              #check every number to see if its a multiple of x
#              for y in range(x*2, N, x):
#                  if y in getallen:
#                      getallen.remove(y)
#          x += 1
#      
#      return getallen
# # 
# =============================================================================
# 
# def priemzeef2(N):
#     priem = list(range(2, N))
#     priemget = []
#     for i in priem:
#         if i % priem[(i-1)] == 0:
#             priemget.append(i)
#             i += 1
#         else:
#             i += 1
#     return priemget
# =============================================================================
# =============================================================================
# 
# def priemzeef(n):
#     zeef = set(range(2,n))
#     lijst = []
#     while zeef:
#         priem = min(zeef)
#         lijst.append(priem)
#         zeef -= set(range(priem, n, priem))
#     return lijst
#     
# =============================================================================

# =============================================================================
# 
# def priemzeef(n):
#     booleanlijst = 
#     van 0 tot n init all true
#     for i in range(2, n**(1/2)):
#         if booleanlijst[i] == True:
#             for j == i ** xi:
#                 booleanlijst[j] = False
#                 x += 1
# 
# =============================================================================


    




            