l=[]
for i in range(100,999):
    for k in range(100,999):
        n=i*k
        if str(n) == str(n)[::-1]:
            l.append(n)
            print i,k,n

print sorted (l),len (l)
#
