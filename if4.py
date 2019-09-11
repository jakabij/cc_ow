year=input("Give the year! ")
if year.isdigit():
	year=int(year)
	if year>=1800 and year<=2099:
		month=["march","april"]
		A=year%19
		B=year%4
		C=year%7
		D=(19*A+24)%30
		E=(2*B+4*C+6*D+5)%7

		if E==6 and D==29:
			H=50
		elif E==6 and D==28 and A>10:
			H=49
		else:
			H = 22 + D + E
			actualMonth=month[0]

		if H>31:
			H=H-31	
			actualMonth=month[1]

		print(actualMonth,H)
	else:
		print("Give a year between 1800 and 2099!")
else:
	print("Give a year, not a string!")
