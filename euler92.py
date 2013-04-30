memo = {89: True, 1:False}
countOfChainsLeadingTo89 = 1

def squareOfDigits(x):
    return sum( [j*j for j in [int(i) for i in str(x)] ] )

def solveChain(x):
    global countOfChainsLeadingTo89
    if x not in memo:
        memo[x] = solveChain(squareOfDigits(x))
        if memo[x]: countOfChainsLeadingTo89 += 1
    return memo[x]
    
[solveChain(i) for i in range(1,10000000)]
print countOfChainsLeadingTo89