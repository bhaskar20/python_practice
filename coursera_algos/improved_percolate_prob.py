'''improved percolate prob using quickfind algos and improved data structure'''

import random
def create_matrix(n):
	'''creates nxn matrix with random true and false initialization depicting open and closed sites'''
	result=[]
	temp=[]
	for i in range(n):
		for j in range(n):
			random_int=random.randint(1,1000)
			if random_int%2==0:
				temp.append(True)
			else:
				temp.append(False)
		result.append(temp)
		temp=[]
	return result

def root(a,flow_matrix,matrix):
	'''a is a tuple with coordinates of element in matrix list and gives the root as a path of element in a list of tuples'''
	i=a[0]
	j=a[1]
	print i,j
	path=[(flow_matrix[i][j])]
	if flow_matrix[i][j]!=None:
		while flow_matrix[i][j]!=(i,j):
				i=flow_matrix[i][j][int(0)]
				j=flow_matrix[i][j][int(1)]
				path.append(flow_matrix[i][j])
	return path
def check_neighbours(i,j,matrix):
	'''takes the coordinates of a element and returns the coordinates of the neighbours with open sites'''
	result=()
	if i==0:
		if matrix[i][j-1]==True:
			result=(i,j-1)
			return result
		else:
			result=(i,j)
			return result
	else:
		if matrix[i-1][j]==True:
			result=(i-1,j)
			return result
		else:
			result=(i,j-1)
			return result
		if matrix[i][j-1]==True:
			result=(i,j-1)
			return result
		else:
			result=(i,j)
			return result

def flow(matrix,n):
	'''gives a matrix with each element connected to root if possible by any path'''
	flow=[]
	temp=[]
	n=len(matrix[0])
	for i in range(n):
		if matrix[i][0]==True:
			temp.append((i,0))
		else:
			temp.append(None)
		for j in range(1,n):
			if matrix[i][j]==True:
				temp.append(check_neighbours(i,j,matrix))
			else:
				temp.append(None)
		flow.append(temp)
		temp=[]
	return flow

def connected():
	'''creates a matrix and checks if it percolates'''
	n=5
	a=create_matrix(n)
	print a
	flow_matrix=flow(a,n)
	print flow_matrix
	result=[]
	for i in range(n):
		if a[i][n-1]==True:
			result.append(root((i,n-1),flow_matrix,a))
	return result
	

print connected()
