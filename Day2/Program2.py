n=int(input("enter nth no"))
a=0
b=1
c=0
count=0
print("fibbonici series upto",n,"th term is following")
while count !=n:
	print(a)
	c=a+b
	a=b
	b=c
	count+=1
	
