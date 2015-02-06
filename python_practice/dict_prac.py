import sys
def word_freq(filename):
	f=open(filename).read().split()
	frequency={}
	for letter in f:
		frequency[letter]=frequency.get(letter,0)+1
	return frequency

#print word_freq(sys.argv[1])

def imp_word_freq(filename):
	f=open(filename).read().split()
	frequency={}
	for letter in f:
		frequency[letter]=frequency.get(letter,0)+1
	for d in sorted(frequency, key=frequency.get ,reverse=True):
		print d, frequency[d]
	return frequency

#print imp_word_freq(sys.argv[1])

def char_count(filename):
	f=open(filename).read()
	frequency={}
	for chars in f:
		if chars!=' ':
			frequency[chars]=frequency.get(chars,0)+1
	return frequency

#print char_count(sys.argv[1])

def valuesort(dicti):
	result=[]
	for d in sorted(dicti):
		result.append(dicti[d])
	return result
#print valuesort({'x': 1, 'y': 2, 'a': 3})


def anagrams(lis):
	''' returns a list containing anagrams from a list of words'''
	copy_lis=lis[:]
	result=[]
	y=[]
	done=[]
	for i in copy_lis:
		if i not in done:
			a=[ chars for chars in i]
			for o in range(lis.index(i),len(lis)):
				print o
				b=[ chars for chars in copy_lis[o]]
				if sorted(a)==sorted(b):
					y.append(lis[o])
					done.append(lis[o])
			result.append(y)
			y=[]
	return result

#print anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node','deno'])


def invertdict(dic):
	result={}
	for keys,values in dic.iteritems():
		result[values]=keys
	return result

#print invertdict({'x': 1, 'y': 2, 'z': 3})













