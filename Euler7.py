import math

def is_prime(x):
    i=2
    sqrt_x=math.floor(math.sqrt(x))    
    while i<=sqrt_x:
        if x%i==0:return False
        i+=1
    return True

prime_count=0
i=1
while prime_count<10001:
    i+=1
    if is_prime(i):
        prime_count+=1

print i