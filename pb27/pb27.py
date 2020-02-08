from math import sqrt
from itertools import chain
import matplotlib.pyplot as plt

def isPremier(n):
    for divisor in range(2, int(sqrt(n)+1)):
        if n%divisor == 0:
            return False
    return True

def listDivisors(n):
    flatten = lambda l: (item for sublist in l for item in sublist)
    l = ((div, n//div) if div != n//div else (div,) for div in range(1, int(sqrt(n)+1)) if n%div == 0)
    return flatten(l)

def displayDivisors(n):
    print('The divisors of %s are: %s' % (n, [i for i in listDivisors(n)]))

def quadraticFormula(a, b, n):
    return n**2 + a*n + b

if __name__ == '__main__':

    plt.figure(figsize=(20,10))
    x = [i for i in range(90)]
    y = [quadraticFormula(1, 41, i) for i in x]
    plt.plot(x,y, label='n²+n+41')
    y = [quadraticFormula(-79, 1601, i) for i in x]
    plt.plot(x,y, label='n²-79n+1601')
    y = [quadraticFormula(-61, 971, i) for i in x]
    plt.plot(x,y, label='n²-61n+971')

    plt.grid(which='major', alpha=0.5), plt.grid(which='minor', alpha=0.2)
    plt.minorticks_on()
    plt.legend()
    plt.savefig('figure.png')
