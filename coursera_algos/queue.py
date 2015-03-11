class queue(object):
	def __init__(self):
		self.data=[]
	def enqueue(self,a):
		if len(self.data)==0:
			self.data.append(a)
		else:
			self.data[1:]=self.data[0:]
			self.data[0]=a
	def dequeue(self):
		self.data.pop()
	def isEmpty(self):
		if len(self.data)==0:
			return True
		else:
			return False

a=queue()
a.enqueue('xx')
a.enqueue('yy')
a.enqueue('zz')
print a.data
a.dequeue()
print a.data
print a.isEmpty()
