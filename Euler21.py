import math

def sum_of_div(x):
    sum=0
    for i in range(1,x/1):
        if x%i==0:
            sum+=i
    return sum

def is_amicable(x):
    a=sum_of_div(x)
    b=sum_of_div(a)
    if b==x and a!=x:
        return True
    else:
        return False

sum=0
for i in range(1,10000):    
    if is_amicable(i):
        sum+=i

print sum