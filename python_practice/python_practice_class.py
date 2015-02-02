def fibonacci_seq(n):
	n1=1
	n2=1
	sum=0
	seq=[]
	while(sum<n):
		sum=n1+n2
		n1=n2
		n2=sum
		if sum<n : 
			print sum
			seq.append(sum)
	return seq
#print fibonacci_seq(30)

def FizzBuzz():
	fizzbuzz={}
	for i in range(1,101):
		if i%3==0:
			if (i%5==0):
				print "FizzBuzz"
				fizzbuzz[i]='FizzBuzz'
			else:
				fizzbuzz[i]='Fizz'
				print "Fizz"
		elif(i%5)==0:
			fizzbuzz[i]='Buzz'
			print "Buzz"
		else:
			fizzbuzz[i]=i
			print i
	return fizzbuzz

print FizzBuzz()

def Collatz(n):
	seq=[]
	while (n>=1):
		print n
		seq.append(n)
		if (n%2==0):
			n/=2
		else:
			n=n*3+1
	return seq

print Collatz(40)



