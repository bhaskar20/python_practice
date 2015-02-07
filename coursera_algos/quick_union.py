a=[]
for i in range(10):
	a.append(i)

print a

def connected(p,q):
	global a
	if a[p]==a[q]:
		return True
	else:
		return False

def connect(p,q):
	global a
	if connected(p,q)==False:
		x=a[q]
		for i in range(len(a)):
			print x
			if a[i]==x:
				a[i]=a[p]
	return a

connect(1,2)
connect(1,2)
print connected(1,9)
print connected(1,7)

print a

