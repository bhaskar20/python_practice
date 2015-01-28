a=[1,2,3,4,5]



def product(a):
	pro=1
	for i in a:
		pro=pro*i
	return pro

x=5
def factorial(x):
	return product(range(1,x+1))

print product(a)
print factorial(x)

def revers(a):
	b=[]
	for i in reversed(a):
		b.append(i)
	return b 

print revers(a)