a= [1,2,3,4,5,6,7,8,9,10,11,12,13,"a","b","c"]
y=10

def split(a,y):
	counter=0
	row=[]
	b=[]
	length=range(len(a))
	for i in length:
		x=a.pop(0)
		if counter<y:
			row.append(x)
			counter=counter+1
		else:
			counter=1
			b.append(row)
			row=[]
			row.append(x)
	b.append(row)

	return b



print split(a,y)
