def sieve(upto):
    l = [True] * upto
    primes = []

    for i in xrange(2, int(upto ** 0.5 + 1.5)):
        if l[i] :
            primes.append(i)
            for k in xrange(i, upto, i):
                l[k] = False
    for j in xrange(2, upto ):
        if l[j]:
            primes.append(j)
    return primes

prime =  sieve(100)
print prime


def factors(numb):
    factor = {}
    nu = numb
    while nu > 1:
        for num in prime:
            if nu % num == 0:
                factor[num] =0
                while nu %num ==0 :
                    factor[num] += 1
                    nu /=num
    return factor

print factors(1000)
