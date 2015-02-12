def exp(x,n):
	if n==0:
		return 1
	else:
		return x*exp(x,n-1)

#print exp(2,3)

def fast_exp(x,n):
	if n==0:
		return 1
	elif n%2==0:
		return fast_exp(x*x,n/2)
	else:
		return x*fast_exp(x,n-1)

def recursive_prod(a,b):
	if b==0:
		return 0
	else:
		return a+recursive_prod(a,b-1)

#print recursive_prod(4,10)

def flat_list(listi,result=None):
	if result is None:
		result=[]
	for x in listi:
		if isinstance(x,list):
			flat_list(x,result)
		else:
			result.append(x)
	return result

#print flat_list([ [1, 2, [3, 4] ], [5, 6], 7])

def flat_dict(dic,result={},key=''):
	for a,b in zip(dic.keys(),dic.values()):
		if isinstance(b,dict):
			flat_dict(b,key=a)
		elif key!='':
			result[key+'.'+a]=b
		else:
			result[a]=b
	return result

#print flat_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})

def unflat_dict(dic):
	result=dict()
	for a,b in dic.iteritems():
		d=result
		print d
		lis=a.split('.')
		for part in lis[:-1]:
			if part not in result:
				d[part]=dict()
			d=d[part]
		d[lis[-1]]=b
	return result
			
#print unflat_dict({'a': 1, 'b.x.1': 2,'b.x.10':4, 'b.y.3': 3, 'c': 4})

def treemap(func,s):
	result=[]
	for a,i in zip(s,range(len(s))):
		if isinstance(a,list):
			print treemap(func,a)
		else:
			result.append(func(a))
	return result

print treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])


