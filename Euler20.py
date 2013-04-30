import math

def fac(x):
    n=1L
    for i in range(2,x+1):
        n*=long(i)
    return n

n=str(fac(100))
sum=0
for i in n:
    sum+=int(i)
print sum