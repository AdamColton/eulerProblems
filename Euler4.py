import math

#find the largest palindrome that is the product of two three digit numbers

def is_palindrome(x):
    x=str(x)
    for i in range(0,len(x)//2):
        if x[i]!=x[len(x)-i-1]: return False
    return True

i=1000
sum=1999
found=False
count=0
while (not found):
    sum-=1
    if sum%2==0: i-=1
    j=i    
    while j<1000:
        count+=1
        if is_palindrome((sum-j)*j):
            print count
            print (sum-j),"x",j,"=",((sum-j)*j)
            found=True
            break
        j+=1