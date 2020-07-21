x= int(input())
n= int(input())
def power(num,n):
	if n <1:
		return 1
	elif(n%2==0):
		return(power(num,n//2)*power(num,n//2))
	else:
		return num*power(num,n//2)*power(num,n//2)
def check(x,n,cur_n=1,cur_s=0):
	result = 0
	p= power(cur_n,n)
	while(p+cur_s<x):
		result+=check(x,n,cur_n,cur_s)
		cur_n+=1
		p=power(cur_n,n)
	if(p+cur_s==result):
		result+=1
		print(cur_n,cur_s)
	return result
print(check(x,n))
