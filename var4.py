num=int(input("Add a number between 1 and 5! "))
print("")
for i in range(1,num+1):
	for j in range(1,num+1):
		print(i*j,end=" ")
	print("")
