a=int(input("Give the height: "))
print("")
j=0
n=2*a-2
for i in range(1,a+1):
	print((n//2)*" " + i*"*" + j*"*"+ (n//2)*" ")
	j=j+1
	n-=2
