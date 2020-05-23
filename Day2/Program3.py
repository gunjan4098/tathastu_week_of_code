for x in range (0,4,1):
	for i in range (0,x,1):
		print (" ",end= ' ')
	for j in range (x,4,1):
		if x==j:
			print("*",end= ' ')
		else:
			print(" ",end= ' ')
	for k in range (x,4,1):
		if k==3:
			print ("*")
		else:
			print(" ",end = ' ')
	print("\r")
for x in range (0,4,1):
	for i in range (3,x,-1):
		print (" ",end= ' ')
	for j in range (0,x+1,1):
		if j==0:
			print("*",end= ' ')
		else:
			print(" ",end= ' ')
	for k in range(0,x+1,1):
		if j==k:
			print("*")
		else:
			print(" ", end=' ')
	
	print("\r")
