m=int(input("Give the column! "))
n=int(input("Give the row! "))
print("")

for i in range(m):
	if i==0 or i==m-1:
		print(n*"*")
	else:
		print("*" + (n-2)*" "+"*")
			
