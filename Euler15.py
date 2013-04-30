def top(x):
	ans=1;
	for i in range(x+1,x*2+1):
		ans*=i
	return ans;
def bottom(x):
	ans=1;
	for i in range(2,x+1):
		ans*=i
	return ans;
	
N=100000 #sides on the grid
print top(N)/(bottom(N))