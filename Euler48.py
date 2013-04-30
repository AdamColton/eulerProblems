# The series, 1^(1) + 2^(2) + 3^(3) + ... + 10^(10) = 10405071317.
# Find the last ten digits of the series, 1^(1) + 2^(2) + 3^(3) + ... + 1000^(1000)

import math

def addNtoThePowerOfN(s,n):
    return (s + n**n)

print reduce(addNtoThePowerOfN, range(1,1001), 0L) % int(1e10)