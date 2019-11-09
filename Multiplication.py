def TwosCompliment(astr):
	#a is a binary number in string form
	# astr=a[2:]
	length=len(astr)
	OnesCompliment=""
	for i in astr:
		if(i=="1"):
			OnesCompliment+="0"
		else:
			OnesCompliment+="1"
	# print(OnesCompliment)
	answer=bin(int(OnesCompliment,2)+int("1",2))
	answer=answer[2:]
	length2=len(answer)
	while(length2<length):
		answer="0"+answer
		length2+=1
	return(answer)

def BinaryAddition(x, y): 
        MaxLength = max(len(x), len(y)) 
  
        x = x.zfill(MaxLength) 
        y = y.zfill(MaxLength) 
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



RegSize=12
Multiplicand=7
SaveMultiplicand=Multiplicand
Multiplier=3
SaveMultiplier=Multiplier

if Multiplier<0:
    Multiplier=bin(Multiplier)[3:]
    
else:
    Multiplier=bin(Multiplier)[2:]

if Multiplicand<0:
    Multiplicand=bin(Multiplicand)[3:]

else:
    Multiplicand=bin(Multiplicand)[2:]


if (len(Multiplicand)<RegSize):
    Multiplicand=(('0'*(RegSize-len(Multiplicand)))+str(Multiplicand))
if (len(Multiplier)<RegSize):
    Multiplier=(('0'*(RegSize-len(Multiplier)))+str(Multiplier))
# NegMultiplicand=TwosCompliment(Multiplicand)
# NegMultiplier=TwosCompliment(Multiplier)

if SaveMultiplicand<0:
    Multiplicand=TwosCompliment(Multiplicand)

if SaveMultiplier<0:
    Multiplier=TwosCompliment(Multiplier)

# print(Multiplicand)
# print(Multiplier)

AC="0"*RegSize
Qn1=0

# print(NegMultiplicand)
# print(NegMultiplier)
# print(AC)



for i in range(RegSize):
    # print(Multiplier)
    if (str(Multiplier[-1]+str(Qn1))=="10"):
        AC=BinaryAddition(AC,TwosCompliment(Multiplicand))[-RegSize:]

    elif(str(Multiplier[-1]+str(Qn1))=="01"):
        AC=BinaryAddition(AC,Multiplicand)[-RegSize:]

    # print(Multiplier)
    



    Qn1=Multiplier[-1]
    Multiplier=Multiplier[:-1]
    Multiplier=AC[-1]+Multiplier
    AC=AC[0]+AC[:-1]


    # print(AC)
    # print(Multiplier)
    # print(Qn1)

# print(AC)
# print(Multiplier)
# print(Qn1)

if(SaveMultiplicand*SaveMultiplier<0):
    print(-int(TwosCompliment(AC+Multiplier),2))
else:
    print(int(AC+Multiplier,2))
# print(TwosCompliment)
# print(int(TwosCompliment(AC+Multiplier),2))
# print()
# print(BinaryAddition("1110","0111")[-4:])