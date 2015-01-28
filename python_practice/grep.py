import sys

def Grep(s,filename):
	f=open(filename).readlines()
	for i in f:
		if s in i:
			print i.strip()

#Grep(sys.argv[1],sys.argv[2])

def Wrap(filename,width):
	lines=open(filename).readlines()
	x=[]
	y=[]
	for i,line in zip(range(len(lines)),lines):
		if len(line)>30:
			x[:30]=line[:30]
			print x
			x[31]="\n"
			x[32:]=line[30:]
			y.append[x]
		else:
			y.append[line]
	w=open(filename,'w')
	w.writelines(y)
	w.close

Wrap(sys.argv[1],sys.argv[2])



