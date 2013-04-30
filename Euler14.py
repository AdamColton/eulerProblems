
dict={}

def sequence(x):
    global dict
    if dict.has_key(x): return dict[x]
    if x==1: return 0
    if x%2==0:
        dict[x]=sequence(x/2)+1
        return dict[x]
    else:
        dict[x]=sequence(3*x+1)+1
        return dict[x]



large=0
ans=0
for i in range(1000000,1,-1):
    temp=sequence(i)
    if temp>large:
        large=temp
        ans=i

print ans