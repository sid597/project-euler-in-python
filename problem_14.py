"this is problem 14"
n = 0


def collatz(nu):
    nm = nu
    ctr = 0
    while nm != 1:
        if nm % 2 == 0:
            nm /= 2
            ctr += 1
        else:
            nm = nm * 3 + 1
            ctr += 1
    return ctr



for i in range(2,1000000):
    seq = collatz(i)
    if seq > n:
        n = seq
        print i, seq

print n, "this is the number"
































