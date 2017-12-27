def factorial(nm):
    a = 1
    for i in xrange(1, nm):
        a *= i
    return a

print sum( [int(i) for i in str(factorial(100))])
