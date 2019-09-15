import click
from time import time
import matplotlib.pyplot as plt

def fibo_naive(n): # return the nth term of fibonacci sequence
    if n < 3:
        return n
    return fibo_naive(n-1) + fibo_naive(n-2)

def fibo_optimized(n):
    if n < 3: return n
    else:
        u = [0] * n
        u[0], u[1] = 1, 2
        for i in range(2, n):
            u[i] = u[i-2] + u[i-1]
        return u[n-1]

def fibo_optimized_2(n):
    if n < 3:
        return n
    fib1, fib2 = 1, 2
    fib3 = fib1 + fib2
    for i in range(3, n):
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib2
    return fib3

def computational_time(fun, n):
    t1 = time()
    fun(n)
    return time() - t1

def answer():
    res = 2
    fib1, fib2 = 1, 2
    fib3 = fib1 + fib2
    while fib3 <= 4*10**6:
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib2
        if fib3%2 == 0:
            res += fib3
    return res

def display(n):
    fig = plt.figure(figsize=(10, 8))
    plt.title('Project Euler - pb2')
    x, y1, y2, y3 = [], [], [], []
    for i in range(1, n+1):
        x.append(i)
        y1.append(computational_time(fibo_naive, i))
        y2.append(computational_time(fibo_optimized, i))
        y3.append(computational_time(fibo_optimized_2, i))
    plt.plot(x, y1, '-o', label='naive (rec)')
    plt.plot(x, y2, '-o', label='optimized (list)')
    plt.plot(x, y3, '-ro', label='optimized (add)')
    plt.minorticks_on() ; plt.legend()
    plt.grid(which='major', alpha=0.8) ; plt.grid(which='minor', alpha=0.2)
    plt.xlabel('Nth term in Fibonacci sequence')
    plt.ylabel('Computational Time (s)')
    plt.savefig('pb2.png')

@click.command()
@click.option('--n', '-n', type=int, required=False, help='nth term in the fibonacci sequence')
def main(n):
    print(answer()) # 4613732

if __name__ == '__main__':
    main()
