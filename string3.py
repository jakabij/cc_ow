string=input("Give the string! ")
newString=[]
for i in range(len(string)):
    newString.append(string[len(string)-1-i])
newString="".join(newString)
print(newString)
