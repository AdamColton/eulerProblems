def continuousFractionSieriesForE(x):
    for i in xrange(x,1, -1):
        if i%3 == 0:
            yield i*2 / 3
        else:
            yield 1
    yield 2

def sumOfDigits(x):
    return sum([int(i) for i in str(x)])

n=1
d=0
for i in continuousFractionSieriesForE(100):
    n,d = i*n+d, n

print sumOfDigits(n)
    