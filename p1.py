from time import time
import click
import matplotlib.pyplot as plt

def naive(N):
    cpt = 0
    for n in range(N):
        if n%3 == 0 or n%5 == 0:
            cpt += n
    return cpt

def optimized(N):
    n1, n2, n3 = (N-1)//3, (N-1)//5, (N-1)//15
    return (3*n1*(n1+1) + 5*n2*(n2+1) - 15*n3*(n3+1))//2

def computation_time(funct, N):
    t1 = time()
    r = funct(N)
    return time() - t1

def computation_time_lists(f1, f2, liste):
    global computation_time
    for x in liste:
        yield computation_time(f1, x), computation_time(f2, x)

def display(x, y):
    fig = plt.figure(figsize=(10,8))
    plt.plot(x, y, '-o')
    plt.savefig('test.png')

@click.command()
@click.option('--number', '-n', type=int, required=False, default=1000, help='number')
@click.option('--start', '-sa', type=int, required=False, default=0, help='start index of the power of 10')
@click.option('--stop', '-so', type=int, required=False, default=3, help='end index of the power of 10')
@click.option('--step', '-se', type=int, required=False, default=1, help='step index of the power of 10')
def main(number, start, stop, step):
    x = [number*10**i for i in range(start, stop, step)]
    y1, y2 = list(zip(*computation_time_lists(naive, optimized, x)))
    plt.figure(figsize=(10,8))
    plt.title('Project Euler - pb1')
    plt.plot(x, y1, '-o', label='naive')
    plt.plot(x, y2, '-ro', label='optimized')
    plt.xlabel('Edge Number') ; plt.ylabel('Computation Time (s)')
    plt.minorticks_on()
    plt.grid(which='major', alpha=0.8) ; plt.grid(which='minor', alpha=0.2); plt.legend()
    plt.savefig('pb1.png')

if __name__ == '__main__':
    main()
