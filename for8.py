n=int(input("Give the number! "))
array=[1]
sum=0
for i in range(1,n):
	array.append(array[i-1]+sum)
	sum=array[i-1]
sum=0
for i in range(n):
	sum+=array[i]

print(sum)
