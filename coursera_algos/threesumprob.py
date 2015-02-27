import random

a=[random.randint(-100,100) for x in range(10)] 

def no_of_three_sum(seq):
	count=0
	for i in range(len(seq)):
		for j in range(i+1,len(seq)):
			for k in range(j+1,len(seq)):
				if (seq[i]+seq[j]+seq[k]==0):
					print seq[i],seq[j],seq[k]
					count+=1
	return count

print no_of_three_sum(a)

def sort(seq):
	'''sort a seq using shellsort'''
	a=seq
	gap=len(seq)//2
	while gap:
		for i,x in enumerate(seq):
			while i>=gap and a[i-gap]>x:
				a[i]=a[i-gap]
				i=i-gap
			a[i]=x
		gap=gap//2
	return seq

def search(seq,key):
	'''return true if key is present in seq'''
	lo=0
	hi=len(seq)-1
	mid=(hi-lo)/2
	while lo<=hi:
		mid=lo+(hi-lo)/2
		if key<seq[mid]:
			hi=mid-1
		else:
			lo=mid+1
	if seq[mid]==key:
		return True
	else:
		return None
		
	

#print search(gen_seq(),10)

def main():
	seq=a
	b=sort(seq)
	count=0
	for i in range(len(b)):
		for j in range(i+1,len(b)):
			find=-(b[i]+b[j])
			if search(b,find)==True:
				print b[i],b[j],find
				count+=1
	return count

print main()
print a




	
