from Twoscompliment import TwosCompliment
def RestoringDivision(Dividend,Divisor):
	# Dividend=bin(Dividend)[2:]
	# Divisor=bin(Divisor)[2:]
	n=len(Dividend)
	Q=Dividend
	M=Divisor
	length=len(M)
	while length<len(Dividend)+1:
		M="0"+M
		length+=1
	MinusM=TwosCompliment(M)
	print(MinusM)
	A="0"*len(M)
	while(n>0):
		print(M,A,Q,n)
		LeftShiftQ=Q[1:]
		A=A[1:]+Q[0]
		print(M,A,LeftShiftQ,n)
		LeftShiftA=bin(int(A,2)+int(MinusM,2))[2:]
		if(len(LeftShiftA)>len(Dividend)+1):
			LeftShiftA=LeftShiftA[::-1]
			LeftShiftA=LeftShiftA[:len(Dividend)+1]
			LeftShiftA=LeftShiftA[::-1]
		elif(len(LeftShiftA)<len(Dividend)+1):
			Temp=len(LeftShiftA)
			while(Temp<len(Dividend)+1):
				LeftShiftA="0"+LeftShiftA
				Temp+=1

		print(M,LeftShiftA,LeftShiftQ,n)
		if(LeftShiftA[0]=="0"):
			A=LeftShiftA
			Q=LeftShiftQ+"1"
		else:
			Q=LeftShiftQ+"0"
		n-=1
		print(M,A,Q,n)
	print(Q,A)
	print(int(Q,2),int(A,2))
if __name__ == '__main__':
	a=1000
	b=504
	print(a,b)
	RestoringDivision(bin(a)[2:],bin(b)[2:])