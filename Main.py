from Multiplication import *
from RestoringDivision import *

if __name__ == '__main__':
	print("Please choose 1 out of the following :")
	print("1. Multiplication")
	print("2. Division")
	i=int(input())
	while(i!=1 and i!=2):
		i=int(input())
	if(i==1):
		print("Multiplcand :",end=" ")
		Multiplicand=int(input())
		print("Multiplier :",end=" ")
		Multiplier=int(input())
		Multiplication(Multiplicand,Multiplier)
	else:
		print("Dividend :",end=" ")
		Dividend=int(input())
		print("Divisor :",end=" ")
		Divisor=int(input())
		RestoringDivision(Dividend,Divisor)