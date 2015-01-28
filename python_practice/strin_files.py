a=["a.c","b.pyc","hh.out","nam.tyc","abs.ja.padhab"]

def extsort(a):
	a.sort(key=lambda s: s.split(".").pop())
	return a

print extsort(a)

f=open('foo.txt')
print open('foo.txt').readlines()

for i in open('foo.txt').readlines():
	print i
	print f.readline()

f = open('foo.txt','a')
f.writelines(open('foo.txt').readlines())
f.close

import sys
print "stop"

def reverse_file(filename):
	f=open(filename).readlines()
	w=open(filename,'w')
	w.writelines(f[::-1])
	w.close
	print open(filename).readlines()

reverse_file(sys.argv[1])





