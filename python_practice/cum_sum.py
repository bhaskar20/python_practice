a=[4,3,2,1,1,3,4,3,8,10]

def cum_sum(a):
	sum=0
	b=[]
	for i in a:
		i=i+sum
		sum=i
		b.append(i)
	return b

print cum_sum(a)


def cum_product(a):
	product=1
	b=[]
	for i in a:
		i=i*product
		product=i
		b.append(i)
	return b

print cum_product(a)
	
