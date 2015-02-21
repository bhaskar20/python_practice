'''a practice module to implement finding best fit line for a univariate regression problem'''
'''We have a list of tuples containing size and price of houses and want to predict price of a house for any particular size'''

import random

class GenerateData:
	'''class to generate random data set of size and prices'''
	def __init__(self):
		self.data=[]
	def initialize(self,n):
		for x in range(n):
			self.data.append((float(random.randint(1,10)),float(random.randint(1,10))))
	
#a=GenerateData()
#a.initialize()
#print a.data

def cost(lis,theta0,theta1):
	'''fn to find the cost'''
	cost=0.0
	print "theta0",theta0
	print "theta1",theta1
	for x in range(len(lis)):
		cost=cost+(((theta0+theta1*lis[x][0]-lis[x][1])*(theta0+theta1*lis[x][0]-lis[x][1]))/2)/len(lis)
	print "Cost",cost
	return cost

def regress(lis):
	'''actual regression is taking place here'''
	#initalized the theta0 and theta1 values
	theta0=0
	theta1=0
	#alpha is the learning rate
	alpha=float(.002)
	#incremental cost to stop the iterations
	inc_cost=20
	temp1=0
	temp2=0
	count=0
	while inc_cost>.1:
		count=count+1
		for x in range(len(lis)):
			#temporary variables to store new theta0 and theta1, differentiated cost wrt theta0 and theta1
			temp1+=(theta0+theta1*lis[x][0]-lis[x][1])/float(len(lis))
			temp2+=((theta0+theta1*lis[x][0]-lis[x][1])*lis[x][0])/float(len(lis))
		print "temp1", temp1
		print "temp2", temp2
		#changed theta0, theta1
		temp1_=theta0-alpha*temp1
		temp2_=theta1-alpha*temp2
		inc_cost=(cost(lis,theta0,theta1)-cost(lis,temp1_,temp2_))
		if inc_cost>=0:
			inc_cost=inc_cost
		else:
			inc_cost=-inc_cost
		theta0=temp1_
		theta1=temp2_
		print "inc_cost",inc_cost
		print '\n'
	print "count",count
	return [theta0,theta1]

def price(size):
	#a=GenerateData()
	#a.initialize(20)
	#learn=a.data
	learn=[(x,x) for x in range(10)]
	print learn
	b=regress(learn)
	price_house=b[0]+b[1]*size
	return price_house

print price(20),"price"





