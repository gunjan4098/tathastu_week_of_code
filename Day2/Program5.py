for i in range(3,0,-1):
	for j in range(i,0,-1):
		if j==i:
			print(i,end= ' ')
		else:
			print("*",i,end= ' ')
	print("\r")
for i in range(1,4,1):
	for j in range(1,i+1,1):
		if j==1:
			print(i,end= ' ')
		else:
			print("*",i,end= ' ')
	print("\r")
