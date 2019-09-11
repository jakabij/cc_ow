string=input("Add the string! ")
newString=[]
for i in range(len(string)):
	newString.append(string[i]+" ")

newString="".join(newString)
print(newString)
