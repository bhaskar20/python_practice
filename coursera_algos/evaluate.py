import stack

def evaluate(s):
	op=stack.stack()
	num=stack.stack()
	for i in s:
		if i.isdigit():
			num.push(int(i))
		elif i=="*":
			op.push(i)
		elif i=="+":
			op.push(i)
		elif i=="-":
			op.push(i)
		elif i==")":
			num1=num.pop()
			num2=num.pop()
			operator=op.pop()
			if operator=="+":
				num.push(num1+num2)
			elif operator=="*":
				num.push(num1*num2)
			else:
				num.push(num1-num2)
		print "OP",op.data
		print "NUM",num.data
	print "OP",op.data
	print "NUM",num.data
	return num.pop()

print evaluate("(((1+2)+(4+3))*9)")