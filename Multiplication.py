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


def Multiplication(Multiplicand,Multiplier):
    output=open("output.txt",'w')
    if Multiplier<0 and Multiplicand <0:
        length=max(len(bin(Multiplicand)[3:]),len(bin(Multiplier)[3:]))
    elif Multiplier>0 and Multiplicand <0:
        length=max(len(bin(Multiplicand)[3:]),len(bin(Multiplier)[2:]))
    elif Multiplier<0 and Multiplicand >0:
        length=max(len(bin(Multiplicand)[2:]),len(bin(Multiplier)[3:]))
    else:
        length=max(len(bin(Multiplicand)[2:]),len(bin(Multiplier)[2:]))

    RegSize=length+1
    SaveMultiplicand=Multiplicand
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

    # NegMultiplier=TwosCompliment(Multiplier)

    if SaveMultiplicand<0:
        Multiplicand=TwosCompliment(Multiplicand)

    if SaveMultiplier<0:
        Multiplier=TwosCompliment(Multiplier)

    NegMultiplicand=TwosCompliment(Multiplicand)
    # print(Multiplicand)
    # print(Multiplier)

    AC="0"*RegSize
    Qn1=0



    for i in range(RegSize):
        # print(Multiplier)
        if (str(Multiplier[-1]+str(Qn1))=="10"):

            AC=BinaryAddition(AC,(NegMultiplicand))[-RegSize:]

        elif(str(Multiplier[-1]+str(Qn1))=="01"):
            AC=BinaryAddition(AC,Multiplicand)[-RegSize:]

        # print(Multiplier)
        



        Qn1=Multiplier[-1]
        Multiplier=Multiplier[:-1]
        Multiplier=AC[-1]+Multiplier
        AC=AC[0]+AC[:-1]
    answer=""
    print("Product in binary form : ",end=" ")
    print(AC+Multiplier)
    answer="Product in binary form : "+str((AC+Multiplier))+'\n'
    if(SaveMultiplicand*SaveMultiplier<0):
        print("Product in decimal form : ",end=" ")
        print(-int(TwosCompliment(AC+Multiplier),2))
        answer=answer+"Product in decimal form : "+str((-int(TwosCompliment(AC+Multiplier),2)))
    else:
        print("Product in decimal form : ",end=" ")
        print(int(AC+Multiplier,2))
        answer=answer+"Product in decimal form : "+str(int(AC+Multiplier,2))
    output.write(answer)
    output.close()


if __name__ == '__main__':
    Multiplier=int(input())
    Multiplicand=int(input())
    Multiplication(Multiplier,Multiplicand)