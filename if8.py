N=int(input("Give how much number do you want! "))
listOfNumbers=[]
for i in range(N):
	num=int(input("Give a number! "))
	listOfNumbers.append(num)

min=listOfNumbers[0]
max=listOfNumbers[0]
for i in range(1,N):
	if min>listOfNumbers[i]:
		min=listOfNumbers[i]
	if max<listOfNumbers[i]:
		max=listOfNumbers[i]

print(min)
print(max)
	

