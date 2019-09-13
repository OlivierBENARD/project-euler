import click
from math import sqrt
from collections import Counter

def proper_divisor(n):
    for divisor in range(1, int(sqrt(n))+1):
        if n%divisor == 0:
            print('(%s, %s)' % (divisor%n, n//divisor))

def somme_divisors(n):
    s = 0
    for divisor in range(1, int(sqrt(n))+1):
        if n%divisor == 0:
            v1, v2 = divisor%n, n//divisor
            if v1 == v2: s += v1
            else: s += v1 + v2
    return s - n

def abundant_numbers(N):
    return [n for n in range(1,N+1) if somme_divisors(n) > n]

def sum_two_abundants(N, abundants): # attention, presence de doublons !
    # res = []
    n = len(abundants)
    for i in range(n):
        for j in range(i, n):
            # res.append(abundants[i]+abundants[j])
            s = abundants[i] + abundants[j]
            if s < N:
                yield abundants[i] + abundants[j]
    # return res

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
    print(sta_without_occurrences)
    res = answer(number, sta_without_occurrences)
    print(res) # not 31531501 neither 4207994
    return None

if __name__ == "__main__":
    main()
