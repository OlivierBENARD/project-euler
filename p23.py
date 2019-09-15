import click
from math import sqrt
from collections import Counter

def divisor(n):
    for divisor in range(1, int(sqrt(n))+1):
        if n%divisor == 0:
            print('(%s, %s)' % (divisor%n, n//divisor))

def somme_divisors(n):
    s = 1 # 1 divide everything
    for divisor in range(2, int(sqrt(n))+1):
        if n%divisor == 0:
            v1, v2 = divisor%n, n//divisor
            if v1 == v2: s += v1 # 9 = 3 * 3 but 3 only have to be added once
            else: s += v1 + v2
    return s

def abundant_numbers(N):
    return [n for n in range(1,N+1) if somme_divisors(n) > n]

def sum_two_abundants(N, abundants): # the generqted list contains occurrences!
    n = len(abundants)
    for i in range(n):
        for j in range(i, n):
            s = abundants[i] + abundants[j]
            if s <= N:
                yield abundants[i] + abundants[j]

def answer(N, sum_two_abundants):
    res = N*(N+1)//2
    for number in sum_two_abundants:
        res -= number
    return res

@click.command()
@click.option('--number', '-n', type=int, help='Number', required=True)
def main(number):
    a = abundant_numbers(number)
    sta = sum_two_abundants(number, a)
    sta_without_occurrences = [k for k in Counter(sta).keys()]
    res = answer(number, sta_without_occurrences)
    print(res) # 4179871
    return None

if __name__ == "__main__":
    main()
