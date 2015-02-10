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
	'''a is a tuples with coordinates of element in matrix list and gives the root as a path of element in a list of tuples'''
	i=a[0]
	j=a[1]
	path=[]
	for a in flow_matrix[i][j]:
		a_i=a[0]
		a_j=a[1]
		sub=[]
		while flow_matrix[a_i][a_j]!=[(a_i,a_j)]:
			sub_path=root((a_i,a_j),flow_matrix,matrix)[2]
			a_i=root((a_i,a_j),flow_matrix,matrix)[0]
			a_j=root((a_i,a_j),flow_matrix,matrix)[1]
			sub.append(sub_path)
			print a_i,a_j
		path.append(sub)
	return a_i,a_j,path


def check_neighbours(i,j,matrix):
	'''takes the coordinates of a element and returns the coordinates of the neighbours with open sites'''
	result=[]
	flag=False
	if i==0:
		if matrix[i][j-1]==True:
			result.append((i,j-1))
		else:
			result.append((i,j))
	flg=False
	if i==len(matrix[0])-1:
		if matrix[i-1][j]==True:
			result.append((i-1,j))
			flg=True
			flag=True
		if matrix[i][j-1]==True:
			result.append((i,j-1))
			flg=True
		if flg==False:
			result.append((i,j))
	if i in range(1,len(matrix[0])-1):
		if matrix[i-1][j]==True:
			result.append((i-1,j))
			flg=True
			flag=True
		if matrix[i][j-1]==True:
			result.append((i,j-1))
			flg=True
		if matrix[i+1][j]==True and flag==False:
			result.append((i+1,j))
			flg=True
		if flg==False:
			result.append((i,j))
	return result


def flow(matrix,n):
	'''gives a matrix with each element connected to root if possible by any path'''
	flow=[]
	temp=[]
	n=len(matrix[0])
	for i in range(n):
		if matrix[i][0]==True:
			temp.append([(i,0)])
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
	n=4
	a=create_matrix(n)
	flow_matrix=flow(a,n)
	for b in flow_matrix:
		print b
	print "\n"
	result=[]
	for i in range(0,n):
		if a[i][n-1]==True:
			result.append(root((i,n-1),flow_matrix,a))
		else:
			result.append(None)
			print "None appended in result"
			print result
	return result
	

print connected()
