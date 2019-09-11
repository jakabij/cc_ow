a=input("Give the a side! ")
b=input("Give the b side! ")
c=input("Give the c side! ")

if a.isdigit() and b.isdigit() and c.isdigit():
	a=int(a)
	b=int(b)
	c=int(c)
	if not(a==0) and not(b==0) and not(c==0):
		if (a**2)+(b**2)==(c**2):
			print("Editable!")
		else:
			print("Not editable!")
	else:
		print("Give non zero sides!")
else:
	print("Only numbers allowed!")
