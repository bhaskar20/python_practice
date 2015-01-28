a=["a","bca","sajnal","abak","1"]

def lensort(a):
	a.sort(key=lambda x: len(x))
	return a

print lensort(a)
