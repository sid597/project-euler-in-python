def factors(nm):
    l = [1]
    for i in xrange(2,int(nm ** 0.5 + 1.5)):
        if nm % i == 0:
            l.append(i)
            l.append(nm/i)
    return sum(l)
print factors(220)


su = 0

for i in xrange(2, 10000):
    s = factors(i)
    if factors(s) == i and i!=s   :
        su += s
        print s,i
print "result is " , su


