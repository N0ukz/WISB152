import operator

#define the operations possible; add them to a dict for easy swaparoo
operatie = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

while True:
    try:
        stack = []
        for i in str.split(input()):
            if i in operatie:
                y, x = stack.pop(), stack.pop()
                z = operatie[i](x, y)
            else:
                z = float(i)
            stack.append(z)
        assert len(stack) <= 1
        if len(stack) == 1 : print(stack.pop())
    except EOFError:    break
    except: print('error')


def rpn_calc(operatie):
    #create an empty list to which we add the temp solutions
    lijst = []
    #ask for imput and itterate through the elements
    for i in str.split(input()):
        #if the element is an operation use it
        if i in operatie:
            #remove the elements from the lijst and add apply the operation to the elements
            y, x = lijst.pop(), lijst.pop()
            z = operatie[i](x, y)
        else:
            z = float(i)
        lijst.append(z)
    #return the final solution
    return lijst.pop()
print(rpn_calc(operatie))

