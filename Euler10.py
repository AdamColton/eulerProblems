import math

def primes(x):    
    # get all primes upto x
    x=int(x)
    if x<2: return []    
    L=[True]*(x-1)
    p=[]
    for i in range(2,int(math.ceil(math.sqrt(x))+1)):
        if L[i-2]:
            p.append(i)
            for j in range(i*i,x+1,i):
                L[j-2]=False
    for i in range(int(math.ceil(math.sqrt(x)))+1,x+1):        
        if L[i-2]:
            p.append(i)
    return p   

p=primes(1000000)

sum=0
for i in p:
    sum+=i
print sum
    
            
        