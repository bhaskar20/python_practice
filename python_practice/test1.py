
def FixStart(s):
	a=s[0]
	new=''
	for letter in s[1:]:
		if letter!=a:
			new=new+letter
		else:
			new=new+'*'
	return a+new

#print FixStart('babble')

def rangeofnum(s):
	list_range=s.split(',')
	result=[]
	for range_no in list_range:
		if len(range_no)>2:
			print len(range_no)
			ind_range=range_no.split("-")
			for i in range(int(ind_range[0]),int(ind_range[1])+1):
				result.append(i)
		else:
			result.append(int(range_no))
	return sorted(result)

#print rangeofnum('8,14,7-10')

def parse(s):
	a=s.split()
	result=[]
	result.append(int(a[2].strip()))
	x=a[1].strip()
	if x=="January" or x=="Jan":result.append(01)
	elif x=="February" or x=="Feb":result.append(02)
	elif x=="March" or x=="Mar":result.append(03)
	elif x=="April" or x=="Apr":result.append(04)
	elif x=="May":result.append(05)
	elif x=="June" or x=="Jun":result.append(06)
	elif x=="July" or x=="Jul":result.append(07)
	elif x=="August" or x=="Aug":result.append(int('08'))
	elif x=="September" or x=="Sep":result.append(int('09'))
	elif x=="October" or x=="Oct":result.append(10)
	elif x=="November" or x=="Nov":result.append(11)
	else:
		result.append(12)
	result.append(int(a[0].strip(',').strip()))
	return tuple(result) 

#print parse('6 March 2013')

def factorialnum(n):
	if n==1:
		return 1
	else:
		return n*factorialnum(n-1)
#print factorialnum(3)
#Error: RuntimeError('maximum recursion depth exceeded',)

def CountChars(s):
	result={}
	for i in s:
		if i in result:
			result[i.lower()]+=1
		if i not in result and i.isalpha():
			result[i.lower()]=1
	return result

#print CountChars('abcdabcd ef')

def CountVowels(s):
	count=0
	vowels=[a,e,i,o,u]
	for i in s:
		if i.lower() in vowels :
			count+=1
	return count

