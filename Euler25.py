last,curr=0L,1L
count=1

while len(str(curr))<1000:
    count+=1
    last,curr=curr,last+curr

print count
