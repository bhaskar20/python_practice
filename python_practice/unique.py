a=[1,2,3,4,5,1,1,2,3,4,5,10,10,"Awe","awe",5,11,11]

def unique(a, key=lambda s: s.lower()):
	b=[]
	for i in a:
		x=key(str(i))
		if x not in b:
			b.append(x)
	return b

print unique(a)

a=[1,2,3,4,5,1,1,2,3,4,5,10,10,"Awe","awe",5,11,11]
def dups(a):
	b=[]
	ran=range(len(a))
	for i in ran:
		x=a.pop()
		if x in a:
			if x not in b:
				b.append(x)
	return b[::-1]

print dups(a)

a=[1,2,3,4,5,1,1,2,3,4,5,10,10,"Awe","awe",5,11,11]
def dup_set(a):
	b=set([])
	for i in a:
		b.add(i)
	return b

print dup_set(a)



