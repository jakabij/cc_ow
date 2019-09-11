pennies= [ ]
print("Give the amount of the crowns. First add how many 5 crowns do you have and press enter. Then add how many 2 and 1 crowns do you have!")
for i in range(3):
	f=int(input("The amount: "))
	pennies.append(f)

crowns=[5,2,1]

result=[ ]
for i in range(3):
	result.append(pennies[i]*crowns[i])

summ=0
for i in range(3):
	summ+=result[i]

print(summ, "crowns")
