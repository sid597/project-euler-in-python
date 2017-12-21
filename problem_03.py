def sieve(primes_upto):
    l = [True] * primes_upto
    primes = []

    for num in xrange(2, int(primes_upto ** 0.5 + 1.5)):
         if l[num] :
            primes.append(num)
            for k in xrange(num, primes_upto, num):

                l[ k] = False
    for i in xrange(2, primes_upto):
        if l[i] == True:
            primes.append(i)
    return primes


l = sieve(int((60085147514 ** 0.5)))

divisors = []

for i in l:
    if 600851475143 % i == 0:
        divisors.append(i)

print divisors
print divisors[-1]
