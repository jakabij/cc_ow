string=input("Give a sentence! ")
tmp=[ ]
for i in range(len(string)):
	if not string[i]==" ":
		tmp.append(string[i])

string="".join(tmp)

print(string)
