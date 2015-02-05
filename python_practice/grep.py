import sys

'''def Grep(s,filename):
	f=open(filename).readlines()
	for i in f:
		if s in i:
			print i.strip()
'''
#Grep(sys.argv[1],sys.argv[2])

def Wrap(filename,width):
	y=[]
	f=open(filename).readlines()
	for i in f:
		line=i.strip()
		if len(line)>width:
			x=line
			no_of_new_lines=len(line)/width
			z=''
			for i in range(no_of_new_lines):
				z=z+''.join([x[:width],'\n'])
				x=line[((i+1)*width):]
			if len(x)>0:
				z=z+x+'\n'
			print z
			y.append(z)
			print y
		else:
			y.append(i)
	print y
	w=open(filename,'w')
	w.writelines(y)
	w.close

#Wrap(sys.argv[1],int(sys.argv[2]))

'''def WordWrap(filename,width):
	f=open(filename).readlines()
	y=[]
	def wrap(f,width):
		for i in f:
			line=i
			if len(line)>width:
				a=line.split()
				x=a[0]
				counter=1
				while (len(x)<width):
					x=x+' '+a[counter]
					counter=counter+1
				x=x+'\n'
				for i in a[(counter+1):]:
					x=x+wrap(i,width)
				y.append(x)
			else:
				y.append(line)
			return y
	wrap(f,width)
	w=open(filename,'w')
	w.writelines(y)
	w.close

WordWrap(sys.argv[1],int(sys.argv[2]))
'''

def WrapSec(words,width):
	'''accepts line as a list and return wrapped line as a string'''
	line=''
	lines=[]
	for i in words:
		com_length=(len(line)+len(i))
		if com_length>int(width):
			lines.append(line)
			line=''
		line=line+i+' '
		if i is words[-1]:lines.append(line+'\n')
	print lines
	return lines






#line=['123','456','789','101112','131415','161718']
#width=10
#print Wrap(line,width)


def WordWrap(filename,width):
	f=open(filename).readlines()
	y=[]
	for lines in f:
		list_words=lines.split()
		y.append("\n".join(WrapSec(list_words,width)))
		print y
	w=open(filename,'w')
	w.writelines(y)
	w.close()

#WordWrap(sys.argv[1],sys.argv[2])

def align(string,width):
	'''gets line as a string and max width of lines in file and returns an aligned string'''
	space=width-len(string)
	if space%2==0:
		string=space/2*' '+string
	else:
		string=(space-1)/2*' '+string
	return string+'\n'

	

def centre_align(filename):
	'''takes a filename and returns a centre aligned file'''
	f=open(filename).readlines()
	max_length=0
	y=[]
	for line in f:
		if len(line.strip())>max_length:max_length=len(line.strip())

	for line in f:
		y.append(align(line.strip(),max_length))
	print y
	w=open(filename,'w')
	w.writelines(y)
	w.close()

centre_align(sys.argv[1])











