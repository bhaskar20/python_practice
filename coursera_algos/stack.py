class stack(object):
	def __init__(self):
		self.data=[]
		
	def push(self,a):
		self.data.append(a)

	def pop(self):
		return self.data.pop()

	def isEmpty(self):
		if len(self.data)==0:
			return True
		else:
			return False

if __name__=="__main__":
	a=stack()
	a.push('aa')
	print a.data
	a.push(2)
	print a.data
	a.pop()
	print a.data
	print a.isEmpty()
	print a
	b=stack()
	b.push('123')
	a.push(b.data)
	print a.data
