'''a practice module to implement finding best fit line for a univariate regression problem'''
'''We have a list of tuples containing size and price of houses and want to predict price of a house for any particular size'''

import random

class GenerateData:
	'''class to generate random data set of size and prices'''
	def __init__(self):
		self.data=[]
	def initialize(self,n):
		for x in range(n):
			self.data.append((float(random.randint(1,1000)),float(random.randint(1,20000))))
	
#a=GenerateData()
#a.initialize()
#print a.data

def cost(lis,theta0,theta1):
	cost=0.0
	print theta0,theta1
	for x in range(len(lis)):
		cost=cost+((theta0+theta1*lis[x][0]-lis[x][1])*(theta0+theta1*lis[x][0]-lis[x][1]))/2*len(lis)
	return cost

def regress(lis):
	theta0=random.randint(1,100)
	theta1=random.randint(1,100)
	alpha=float(100)
	inc_cost=20
	temp1=0
	temp2=0
	while inc_cost>1 or inc_cost<-1:
		print 10
		for x in range(len(lis)):
			temp1+=-(theta0+theta1*lis[x][0]-lis[x][1])/len(lis)
			temp2+=-(theta0+theta1*lis[x][0]-lis[x][1])*lis[x][1]/len(lis)
		temp1_=theta0-alpha*temp1
		temp2_=theta1-alpha*temp2
		inc_cost=cost(lis,theta0,theta1)-cost(lis,temp1_,temp2_)
		theta0=temp1_
		theta1=temp2_
		print inc_cost
		print "hehr"
	return [theta0,theta1]

def price(size):
	a=GenerateData()
	a.initialize(2)
	learn=a.data
	b=regress(learn)
	price_house=b[0]+b[1]*size
	return price_house

print price(10)





