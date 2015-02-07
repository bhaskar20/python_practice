a=[x for x in range(10)]

def connected(p,q):
	root_p=root(p)
	root_q=root(q)
	return root_p==root_q

def connect(p,q):
	if connected(p,q)==False:
		a[root(p)]=a[root(q)]

def root(p):
	i=a[p]
	while a[i]!=i:
		i=a[i]
	return i

connect(1,2)
connect(1,3)
connect(1,9)
connect(1,8)
connect(4,3)
connect(8,9)
print a
print connected(3,8)
print connected(2,3)
print connected(1,9)
print connected(1,7)




		

