string=input("Give a sentence! ")
spaces=0

for i in range(len(string)):
	if string[i]==" ":
		spaces+=1

print("The space number: ",spaces)
