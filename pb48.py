import time

# python3 pb48.py > res.txt
def pb48(n):
    res = sum((i**i for i in range(1, n+1)))
    print(str(res)[-10:])

t1 = time.time()
pb48(100)
print(time.time()-t1)
t1 = time.time()
pb48(1_000)
print(time.time()-t1)
t1 = time.time()
pb48(10_000)
print(time.time()-t1)
