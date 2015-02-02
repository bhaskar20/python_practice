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

def WordWrap(filename,width):
	f=open(filename).readlines()
	print f
	y=[]
	for i in f:
		line=i.strip()
		print line 
		if len(line)>width:
			a=line.split()
			print a
			x=''
			counter=0
			while (len(x)<width):
				x=x+"".join(a[counter])
				print x
				print len(x)
				print counter
				counter=counter+1
			print counter
			x=x+'\n'
			for i in a[(counter+1):]:
				x=x+i
			print x
			y.append(x)
		else:
			y.append(line)
		w=open(filename,'w')
		w.writelines(y)
		w.close

WordWrap(sys.argv[1],int(sys.argv[2]))
