#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# 354294 this is the largest possible number
# 354294 =9^5+9^5+9^5+9^5+9^5+9^5 for 999999

def isSumOfFifthPower(i):
    temp_string = str(i)
    for j in range(0, len(temp_string)):
        sum += int(temp_string[j])**5
    return (sum==i)
        
answer=0
for i in range(10,354294):
    sum=0
    temp_string=str(i)
    for j in range(0,len(temp_string)):
        sum+=int(temp_string[j])**5
    if (sum==i):
        answer+=i
print "Answer: "+str(answer)
    
