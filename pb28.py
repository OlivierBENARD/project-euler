def pb28(diag_len):
    sum = 0
    position = {}
    for diag in range(3, diag_len+1, 2):
        position[diag*diag] = diag-1
    for pos in position:
        sum += decomp(pos, position[pos])
    print(sum+1)

def decomp(n, ecart):
    return sum(i for i in range(n, n-4*ecart, -ecart))

pb28(1001)
