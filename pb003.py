import click
from math import sqrt

def divisors(n):
    return [i for d in range(1, int(sqrt(n)+1)) if n%d == 0 for i in (d, n//d)]

def isPrime(n):
    return len(divisors(n)) == 2

def listPrimes(n):
    return [i for i in range(1, n+1) if isPrime(i)]

@click.command()
@click.option('--number', '-n', type=int, help='number to look for')
def main(number):
    l = divisors(number)
    cpt = 0
    for e in l:
        if isPrime(e):
            if e > cpt:
                cpt = e
    print(cpt)

if __name__ == '__main__':
    main()
