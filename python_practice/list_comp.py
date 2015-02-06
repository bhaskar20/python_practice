import sys

def zip(a,b):
	return [(a[x],b[y]) for x in range(len(a)) for y in range(len(b)) if x==y ]

#print zip([1,2,3],['a','b','c'])

def square(x): return x*x

def map(function,n):
	return [ function(i) for i in n]

#print map(square,range(5))

def even(x): return x%2==0
def filter(fn,a):
	return [ i for i in a if fn(i)]

#print filter(even,range(10))

def triplets(n):
	return [(a,b,c) for a in range(1,n) for b in range(a,n) for c in range(b,n) if a+b==c]

#print triplets(5)

def enumerate(lis):
	return [(index,item) for index in range(len(lis)) for item in lis if lis[index]==item ]

#print enumerate(['a','b','c'])

def array(row,column):
	a=[]
	for x in range(row):
		a.append([])
		for y in range(column):
			a[x].append(None)
	return a

#print array(3,4)

def parse_csv(filename):
	f=open(filename).readlines()
	result=[]
	for lines in f:
		a=lines.split(',')
		print a
		result.append([ x.strip() for x in a ])
	return result

#print parse_csv(sys.argv[1])

def improved_parse(filename,delim):
	f=open(filename).readlines()
	result=[]
	for lines in f:
		if lines.strip()[0] !='#':
			a=lines.split('delim')
			print a
			result.append([ x.strip() for x in a ])
	return result

#print improved_parse(sys.argv[1],sys.argv[2])

def mutate(word):
	'''inserting a character, deleting a character, replacing a character, or swapping 2 consecutive characters in a string'''
	dicta=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
	result=[word]
	for i in range(len(word)+1):
		for x in dicta:
			result.append(word[0:i]+x+word[i:])
	for i in range(len(word)+1):
		for x in dicta:
			result.append(word[0:i]+x.upper()+word[i:])
	for i in range(len(word)):
		result.append(word[0:i]+word[i+1:])
	for i in range(len(word)):
		for a in dicta:
			result.append(word[0:i]+a+word[i+1:])
	for i in range(len(word)):
		for a in dicta:
			result.append(word[0:i]+a.upper()+word[i+1:])
	for i in range(len(word)-1):
		result.append(word[0:i]+word[i+1]+word[i]+word[i+2:])
	return result


	
'''print 'hello' in mutate('hello')
print 'ehllo' in mutate('hello')
print 'cello' in mutate('hello')
print 'ahello' in mutate('hello')
print 'Ahello' in mutate('hello')	
print mutate('hello')'''

def nearly_equal(a,b):
	if a in mutate(b):
		return True
	else:
		return False

print nearly_equal('python','perl')
print nearly_equal('perl', 'pearl')
print nearly_equal('python', 'jython')
print nearly_equal('man', 'woman')

