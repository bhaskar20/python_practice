import sys

def reverselines(filename):
	f=open(filename).readlines()
	for str,i in zip(f,range(len(f))):
		x=[str[::-1].strip(),'\n']
		f[i]=" ".join(x)
	w=open(filename,'w')
	w.writelines(f)
	w.close()

reverselines(sys.argv[1])

def Head(filename):
	f=open(filename).readlines()
	if len(f)<10:
		print open(filename).read()
	else:
		f=open(filename).readlines()
		x=''
		for i in f[:10]:
			x=x+"".join(i)
		print x.strip()

Head(sys.argv[1])
print "here"

def Tail(filename):
	f=open(filename).readlines()
	if len(f)<10:
		print open(filename).read()
	else:
		f=open(filename).readlines()
		x=''
		length=len(f)
		for i in f[(length-10):]:
			x=x+"".join(i)
		print x.strip()

Tail(sys.argv[1])