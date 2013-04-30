import math

def is_prime(x):
    i=2
    sqrt_x=math.floor(math.sqrt(x))    
    while i<=sqrt_x:
        if x%i==0:return False
        i+=1
    return True

N=317584931803
i=math.floor(math.sqrt(N))
found=False
while not found:
    if N%i==0:
        if is_prime(i):        
            found=True
            break
    i-=1

print i



        