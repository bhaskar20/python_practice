import random

a=[1,2,5,342,1,213,12,12,13124,1534,24,3546,657,3424,1]

def slectionsort(a):
	for i in range(len(a)):
		min=a[i]
		x=i
		for j in range(i,len(a)):
			if a[j]<min:
				min=a[j]
				x=j
		a[x]=a[i]
		a[i]=min
	return a

#print slectionsort(a)

def insertionsort(a):
	for i in range(1,len(a)):
		val=a[i]
		j=i-1
		while j>=0 and a[j]>val:
			a[j+1]=a[j]
			j=j-1
		a[j+1]=val
	return a

#print insertionsort(a)

def shellsort(a):
	gap=len(a)//2
	while gap:
		for i,x in enumerate(a):
			while i>=gap and a[i-gap]>x:
				a[i]=a[i-gap]
				i=i-gap
			a[i]=x
		gap=gap//2
	return a

#print shellsort(a)

def bubblesort(a):
	for i in range(len(a)):
		for j in range(i,len(a)):
			if a[i]>a[j]:
				a[j],a[i]=a[i],a[j]
	return a

#print bubblesort(a)





		

















