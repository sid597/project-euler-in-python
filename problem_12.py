'''
first make a list of all primes upto a large number
then for each triangle number do its prime factorisation
then from the list of prime factors of the trianglr number calculate the number
factors


'''


def sieve(upto):
    '''
    Sieve to make a list of all factors
    '''

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

prime =  sieve(1000000)


def factors(numb):
    '''
    Returns Dictionary of factors in format
    {prime factor: its occurence}
    for example for prime factors of 8 this
    will return a dictionary as
    {2:3} i.e 8 = 2*2*2
    '''
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


def no_of_factors(di):

    '''
    Calculates the number of prime factors by a given dict
    for example :
        100 = (2 ** 2) * (5 ** 2)
        so number of factors are =(2+1) * (2+1)

    '''
    kys  = di.values()
    p = 1
    for num in kys :
        p *= (num + 1)
    return p

s = 0
n = 1

'''
Generating triangular numbers
and calculating the no of factors
'''
for i in xrange(2, 10000000):
    n += i
    nos = no_of_factors(factors(n))
    if nos > s:
        s = nos
        print n, nos


'''
Some results
3 2
6 4
28 6
36 9
120 16
300 18
528 20
630 24
2016 36
3240 40
5460 48
25200 90
73920 112
157080 128
437580 144
749700 162
1385280 168
1493856 192
2031120 240
2162160 320
17907120 480
76576500 576
103672800 648
236215980 768
842161320 1024
3090906000 1280
4819214400 1344
7589181600 1512
7966312200 1536

'''

