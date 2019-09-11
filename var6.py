money=int(input("Give the amount! "))
print("")
crowns=[10,5,2,1]
canPay=[]

canPay.append(money//crowns[0])
leftOver=money%crowns[0]
for i in range(1,4):
	canPay.append(leftOver//crowns[i])
	leftOver=leftOver%crowns[i]		

for i in range(4):
	print("From %d crowns: " %crowns[i],(canPay[i]))
