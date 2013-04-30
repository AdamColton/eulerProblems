import math

# A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,
# a² + b² = c²
#
# For example, 3² + 4² = 9 + 16 = 25 = 5².
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def f(x):
    # Given: a²+b²=c² and a+b+c=1000
    # then: c=100-a-b :.
    # a²+b²=(1000-a-b)² :.
    # a²+b²=1000000-1000a-1000b-1000a-a²+ab-1000b+ab+b² :.
    # 0=1000000-2000a-2000b+2ab :.
    # a=(1000000-2000b)/(2000-2b)
    x=float(x)
    return (1000000-2000*x)/(2000-2*x)

a=0
b=1.1
while math.modf(b)[0]!=0:
    a+=1
    b=f(a)

c=math.sqrt(a**2+b**2)

print a*b*c
print a