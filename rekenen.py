#define a function "wortel" that approximates the value of a sqrt
def wortel(a, epsilon):
   k = 0 # k will count the amount of itterations, if its 100 it will stop
   x_k = a # initial value of x
   while abs(x_k ** 2 - a) > epsilon and not k == 100:
        x_k = 1/2 * ( x_k + a * x_k ** (-1))
        k += 1
   return x_k