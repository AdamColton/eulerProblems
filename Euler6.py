import math

sum_of_squares=square_of_sum=0

for i in range(1,101):
    sum_of_squares+=math.pow(i,2)
    square_of_sum+=i

square_of_sum=math.pow(square_of_sum,2)
difference=square_of_sum-sum_of_squares
print difference