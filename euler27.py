from math import sqrt

def functional(func):
    def build(*x):
        try:
            if x not in func.D:              #check if value exists in the functions dictionary
                func.D[x] = func(*x)     #if its not there, calculate
        except:                          #if the function doesn't have a dictionary defined yet
            func.D = {}                  #create dictionary
            func.D[x] = func(*x)         #calculate value for x
        return func.D[x]                 #return value
    return build

@functional
def is_prime(x):
    if x < 0: return False
    for i in xrange(2,int(sqrt(x))):
        if is_prime(i) and ( x % i == 0 ):
            return False
    return True

def numberOfPrimesProduced(a,b):
    q = lambda n: n**2 + a*n + b
    n = 0
    while is_prime( q(n) ):
        n += 1
    return n

bestAnswer = None
primeCountOfBestAnswer = 0
for a in xrange(-1000, 1000):
    for b in xrange(-1000, 1000):
        primeCount = numberOfPrimesProduced(a,b)
        if primeCount > primeCountOfBestAnswer:
            primeCountOfBestAnswer = primeCount
            bestAnswer = (a,b)

print "Best Answer: ", bestAnswer
print "Primes Produced: ", primeCountOfBestAnswer
print "Answer to Euler 27: ", bestAnswer[0] * bestAnswer[1]