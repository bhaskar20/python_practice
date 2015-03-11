a=[1,2,10,24,23,12,45,32,56,34,23,5,7,8,34,54,656]
b=[34,3,4,5,6,7,34,23,234,234,23,5,76,78,56,8,545,4552,23,24,78,76,9,45,42,12,16,-1,100000,9999999999,2,657]
a.sort()
b.sort()
print a,b

def merge(a,b):
	result=[]
	ri=0
	ai=0
	bi=0
	while len(a)>0 and len(b)>0:
		if a[ai]<b[bi]:
			result.append(a[ai])
			a.remove(a[ai])
		elif a[ai]==b[bi]:
			result.append(a[ai])
			a.remove(a[ai])
		else:
			result.append(b[bi])
			b.remove(b[bi])
	if len(a)>0:
		for i in a:
			result.append(i)
	if len(b)>0:
		for i in b:
			result.append(i)
	return result
print merge(a,b)

def mergesort(alist):
	if len(alist)>1:
		mid=len(alist)//2
		lefthalf=alist[:mid]
		righthalf=alist[mid:]

		mergesort(lefthalf)
		mergesort(righthalf)
		i=0
		j=0
		k=0
		merge(lefthalf,righthalf)
	return alist

print mergesort([34,3,4,5,6,7,34,23,234,234,23,5,76,78,56,8,545,4552,23,24,78,76,9,45,42,12,16,-1,100000,9999999999,2,657])			

