for x in range (0,5,1):
	for y in range (x,5,1):
		print ("*",end= ' ')
	for k in range(0,x,1):
		print("  ",end= ' ')
	print(" ",end= ' ')
	for i in range (0,x,1):
		print("  ",end= ' ')
	for j in range(x,5,1):
		print("*",end=' ')
	print ("\r")
for x in range (0,5,1):
	for y in range (0,x+1,1):
		print("*", end= ' ')
	for k in range (x,4,1):
		print("  ",end=' ')
	print(" ",end= ' ')
	for i in range(x,4,1):
		print("  ",end= ' ')
	for j in range(0,x+1,1):
		print("*",end= ' ')
	print("\r")
