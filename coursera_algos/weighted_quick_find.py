a=[x for x in range(10)]
sz=[ 1 for x in range(10)]

def connected(p,q):
	return root(p)==root(q)

def connect(p,q):
	root_p=root(p)
	root_q=root(q)
	if sz[root_p]>sz[root_q]:
		a[root_q]=a[root_p]
		sz[root_p]+=sz[root_q]
	elif sz[root_q]>sz[root_p]:
		a[root_p]=a[root_q]
		sz[root_q]+=sz[root_p]
	else:
		a[root_q]=a[root_p]
		sz[root_p]+=sz[root_q]



def root(p):
	i=a[p]
	while a[i]!=i:
		a[i]=a[a[i]]
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