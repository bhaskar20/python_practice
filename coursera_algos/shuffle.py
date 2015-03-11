a=[2,3,5,7,10,'K','Q','j',4,10]
import random
def good_shuffle(a):
	for i,x in enumerate(a):
		rand=random.randint(0,i)
		a[i]=a[rand]
		a[rand]=x
	return a

print good_shuffle(a)

def bad_shuffle(a):
	b=[]
	result=[]
	for i in range(len(a)):
		b.append(random.random())
	x=sorted(b)
	for i,val in enumerate(a):
		pos=b.index(x[i])
		result.append(a[pos])
	return result

print bad_shuffle(a)


