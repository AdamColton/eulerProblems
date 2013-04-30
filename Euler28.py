corner=[3,5,7,9]
delta=[2,4,6,8]
delta_prime=8
sum=1+3+5+7+9

while corner[3]<1002001:
    for i in range(0,4):
        delta[i]+=delta_prime
        corner[i]+=delta[i]
        sum+=corner[i]
print sum