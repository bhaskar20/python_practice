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

print slectionsort(a)

def insertionsort(a):
	for i in range(1,len(a)):
		val=a[i]
		j=i-1
		while j>=0 and a[j]>val:
			a[j+1]=a[j]
			j=j-1
		a[j+1]=val
	return a

print insertionsort(a)

def shellsort(a):
	pass
def bubblesort(a):
	pass
def quicksort(a):
	pass
def mergesort(a):
	pass
def bottomupmergesort(a):
	pass
def heapsort(a):
	pass




		

















