from Twoscompliment import TwosCompliment

def BinaryAddition2(x, y): 
	MaxLength=len(x)
	result = '' 
	carry = 0
	for i in range(MaxLength - 1, -1, -1): 	
		r = carry 
		if (x[i] == '1'):
			r=r+1
		if (y[i] == '1'):
			r=r+1
		if(r % 2 == 1):
			result="1"+result
		else:
			result="0"+result
		if (r<2):
		    carry=0
		else:
		    carry=1 
	if (carry!=0):
		result="1"+result
	return result.zfill(MaxLength)



def RestoringDivision(Dividend,Divisor):
	if Divisor==0:
		print("ZeroDivisionError : Divisor cant be zero")
		return
	elif Dividend==0:
		print("Quotient and Remainder in binary form:",0,0)
		print("Quotient and Remainder in decimal form:",0,0)
		return
	DividendSignPlus=True
	DivisorSignPlus=True
	if(Dividend<0):
		Dividend*=-1
		DividendSignPlus=False
	if(Divisor<0):
		Divisor*=-1
		DivisorSignPlus=False
	Dividend=bin(Dividend)[2:]
	Divisor=bin(Divisor)[2:]
	n=len(Dividend)
	Q=Dividend
	M=Divisor
	length=len(M)
	while length<len(Dividend)+1:
		M="0"+M
		length+=1
	MinusM=TwosCompliment(M)
	# print(MinusM)
	A="0"*len(M)
	while(n>0):
		# print(M,A,Q,n)
		LeftShiftQ=Q[1:]
		A=A[1:]+Q[0]
		# print(M,A,LeftShiftQ,n)
		# LeftShiftA=bin(int(A,2)+int(MinusM,2))[2:]
		LeftShiftA=BinaryAddition2(A,MinusM)
		if(len(LeftShiftA)>len(Dividend)+1):
			LeftShiftA=LeftShiftA[::-1]
			LeftShiftA=LeftShiftA[:len(Dividend)+1]
			LeftShiftA=LeftShiftA[::-1]
		elif(len(LeftShiftA)<len(Dividend)+1):
			Temp=len(LeftShiftA)
			while(Temp<len(Dividend)+1):
				LeftShiftA="0"+LeftShiftA
				Temp+=1
		# print(M,LeftShiftA,LeftShiftQ,n)
		if(LeftShiftA[0]=="0"):
			A=LeftShiftA
			Q=LeftShiftQ+"1"
		else:
			Q=LeftShiftQ+"0"
		n-=1
		# print(M,A,Q,n)
	if(DividendSignPlus and DivisorSignPlus):
		print("Quotient and Remainder in binary form:",Q,A)
		print("Quotient and Remainder in decimal form:",int(Q,2),int(A,2))
	elif(DividendSignPlus and not(DivisorSignPlus)):
		print("Quotient and Remainder in binary form:",TwosCompliment(Q),A)
		print("Quotient and Remainder in decimal form:",-int(Q,2),int(A,2))
	elif(not(DividendSignPlus) and DivisorSignPlus):
		print("Quotient and Remainder in binary form:",TwosCompliment(Q),TwosCompliment(A))
		print("Quotient and Remainder in decimal form:",-int(Q,2),-int(A,2))
	else:
		print("Quotient and Remainder in binary form:",Q,TwosCompliment(A))
		print("Quotient and Remainder in decimal form:",int(Q,2),-int(A,2))

if __name__ == '__main__':
	a=int(input())
	b=int(input())
	RestoringDivision(a,b)
	print(BinaryAddition2("0111","0111"))
	print(bin(int("0111",2)+int("0111",2))[2:])