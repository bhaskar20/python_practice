a=[1,2,5,342,1,213,12,12,13124,1534,24,3546,657,3424,1]

b=sorted(a)

def binarysearch(x,seq):
	print seq
	lo=0
	hi=len(seq)-1
	while lo<=hi:
		mid=lo+(hi-lo)/2
		if x<seq[mid]:
			hi=mid-1
		elif x>seq[mid]:
			lo=mid+1
		else:
			return mid

#print binarysearch(13124,b)

def binarysearchrec(x,seq):
	print seq
	if len(seq)==0:
		return False
	elif len(seq)==1 and seq[0]!=x:
		return False
	else:
		mid=len(seq)/2
		if seq[mid]==x:
			return True
		else:
			if x>seq[mid]:
				return binarysearchrec(x,seq[mid+1:])
			else:
				return binarysearchrec(x,seq[:mid])

print binarysearchrec(13124,b)
		



