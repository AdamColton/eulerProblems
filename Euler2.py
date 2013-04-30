import math
print "### START ###"
last=curr=1.0
sum=0
while curr<1000000:
    if curr%2==0:
        sum=sum+curr
    last,curr=curr,curr+last

print sum