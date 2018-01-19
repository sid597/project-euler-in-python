a = 1
b = 1
c = a+b
ctr = 0

while len(str(c)) < 1000:
    a = b
    b = c
    c = a + b
    ctr += 1

print ctr


