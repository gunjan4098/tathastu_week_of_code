no=int(input("enter a no"))
#for even and odd no
if no%2==0 :
	print ( no," is even no")
else :
	print ( no," is odd no")
#for prime no
s=0
for x in range(1,no+1,1) :
	if no%x==0 :
		s+=1
if s==2 :
	print (no," is prime no")
else :
	print(no," is not prime no")
#for palindrome
length=0
r=0
n=no
while n>0 :
	d=n%10
	n=n // 10
	r=(r*10)+d
	length+=1
if r==no :
	print (no," is pallindrome")
else:
	print(no,"  is not pallindrome")
# for armstrong no
sum=0
temp=no
while temp>0 :
	d=temp%10
	temp =temp // 10
	sum= sum + (d ** length)
if sum==no:
	print(no,"is armstrong no")
else:
	print(no,"is not armstrong no")
	
