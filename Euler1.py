jumps=[3,2,1,3,1,2,3] #these steps will give you every multiple of 3 an 5

n=0
sum=0
below_oneK="true"
while below_oneK=="true":
    for i in jumps:
        if n+i<1000:
            n=n+i
            sum=sum+n
            print n
        else:
            below_oneK="false"
            break;

print sum
            