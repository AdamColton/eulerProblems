def fac(x):
    if x<=1: return 1
    return fac(x-1)*x

def isCurious(x):
    return sum([fac(int(c)) for c in str(x)]) == x

print [i for i in range(3,10**6) if isCurious(i)]

        
