'''
This is brute force solution with O(n**3) complexity
the three nos are 200,375,425
'''

for i in range(1,1000):
    for j in range(i,1000):
        for k in range(j,1000):
            if (i+j+k == 1000) and (i**2 + j**2 == k**2 ):
                print i,j,k , i*j*k

