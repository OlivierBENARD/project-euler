import itertools
import time

# lim x -> infini de somme k = 0 a x de a_k/10^k
def developpement_decimal(a,b):
    q, r = a//b, a  # si le reste est deja vu, on boucle : le developpement decimal est infini periodique. On s'arrete.
    r_dejavu = [] # sinon s'il est nul : la division est à dev. dec. fini
    cycle = []
    cycle.append(q) # on ajoute a0
    while r != 0 and (r not in r_dejavu):
        r_dejavu.append(r) # on ajoute le nouveau reste
        nb_zero = 0
        while (r < b):
            r *= 10
            nb_zero += 1
        for _ in range(nb_zero-1): # on decalle d'autant de 0
            cycle.append(0)
        q, r = (r//b, r%b)
        cycle.append(q) # on ajoute le quotient
    return cycle

def recurring_cycle_length(liste, elem):
    n = len(liste)
    first_pos = 0
    for i in range(n):
        if liste[i] == elem:
            first_pos = i
    return n - first_pos

def naive(d):
    q, r = 1//d, 1
    r_dejavu = [] # si le reste est deja vu, on boucle : le developpement decimal est infini periodique ; sinon s'il est nul : la division est à dev. dec. fini
    cycle = []
    cycle.append(q) # on ajoute a0
    nb_decallages = 0
    while r != 0 and (r not in r_dejavu):
        r_dejavu.append(r) # on ajoute le nouveau reste
        nb_zero = 0
        while (r < d):
            r *= 10
            nb_zero += 1
        nb_decallages += (nb_zero - 1)
        for _ in range(nb_zero-1): # on decalle d'autant de 0
            cycle.append(0)
        q, r = (r//d, r%d)
        cycle.append(q) # on ajoute le quotient
    len = 0 # calcul de la longueur du cycle en prenant en compte les decallages de x10 (voir exemple 1/999)
    if r != 0:
        len = recurring_cycle_length(r_dejavu, r) + nb_decallages
    return len

def pb26_naive(lim=1000):
    max_len = 0
    d_max = 0
    for d in range(2, lim):
        tmp_len = naive(d)
        if tmp_len > max_len:
            max_len = tmp_len
            d_max = d
    print('1/%s has a %s-digit recurring cycle' % (d_max, max_len))

def optimized(d): # renvoi la longueur de la periode
    r = 10
    seen = {}
    for i in itertools.count(0):
        if r == 0: # developpement decimal limite non periodique
            return 0
        elif r in seen:
            return i - seen[r] # current position - first_position
        seen[r] = i # stocke la position a laquelle on avait vu le reste
        r = 10*(r%d)

def pb26_optimized(lim=1000):
    len, i = max((optimized(i), i) for i in range(2, lim))
    print('1/%s has a %s-digit recurring cycle' % (i, len))

if __name__ == '__main__':
    t2 = time.time()
    pb26_optimized(1000)
    print('Optimized:\n%s' % (time.time() - t2))
    t1 = time.time()
    pb26_naive(1000)
    print('Naive:\n%s' % (time.time() - t1))
