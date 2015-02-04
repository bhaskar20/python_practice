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

def Wrap(line,width):
	'''accepts line as a list and return wrapped line as a string'''
	y=''
	flag=False
	for i in range(len(line)):
		a=line[i]
		print a
		while len(y) < width:
			print len(y)<width
			print len(y)
			print width
			y=y+' '+a
			print y
			y=y+'\n'
			flag=True
		if flag and len(line)>0:
			Wrap(line,width)
			print y
	return y


def WordWrap(filename,width):
	f=open(filename).readlines()
	y=[]
	for lines in f:
		list_words=lines.split()
		y.append(Wrap(list_words,width))
	w=open(filename,'w')
	w.writelines(y)
	w.close()

WordWrap(sys.argv[1],sys.argv[2])



