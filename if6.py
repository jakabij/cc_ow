#A little bit modified exercise that cut off all '>' and '<' signs

string=input("Give a sentence! ")
newString=[]
for i in range(len(string)):
	if string[i]=="<":
		i+=1
		if not((string[i]=="<")):
			while not(string[i]==">"):
				newString.append(string[i])
				i+=1
			if newString:	
				str1="".join(newString)
				print(str1)
				newString=[]
