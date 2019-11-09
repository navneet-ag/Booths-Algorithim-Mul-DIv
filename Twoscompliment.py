def TwosCompliment(a):
	#a is a binary number in string form
	astr=a[2:]
	length=len(astr)
	OnesCompliment=""
	for i in astr:
		if(i=="1"):
			OnesCompliment+="0"
		else:
			OnesCompliment+="1"
	print(OnesCompliment)
	answer=bin(int(OnesCompliment,2)+int("1",2))

	answer=answer[2:]
	length2=len(answer)
	while(length2<length):
		answer="0"+answer
		length2+=1
	return(answer)

a=int(input())
a=bin(a)
print(a[2:])
print(TwosCompliment(a))