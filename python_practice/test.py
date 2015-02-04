def fibonacci(n):
	seq=[]
	num1=0
	num2=1
	su=0
	seq.append(num1)
	seq.append(num2)
	while (len(seq)<n):
		su=num2+num1
		if (len(seq)<n):seq.append(su)
		num1=num2
		num2=su
	return seq

print fibonacci(8)



		