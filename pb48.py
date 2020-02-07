# python3 pb48.py > res.txt
def pb48(n):
    res = sum((i**i for i in range(1, n+1)))
    print(str(res)[-10:])

pb48(1000)
