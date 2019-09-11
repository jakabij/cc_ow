N=int(input("How much number do you want to add? "))

conjugate=0
impair=0
impair_sum=0
for i in range(N):
	a=int(input("Give a number! "))
	if a%2==0:
		conjugate+=1
	else:
		impair+=1
		impair_sum+=a

print("The count of conjugate/conjugates: ",conjugate, "The count of impair/impairs: ",impair,"The sum of the impairs: ",impair_sum)

