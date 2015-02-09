''' percolation probelem model for monte carlo simulations very basic model
	hasn't implemmented quick find algos or any improvements
'''
import random

matrix=[]
n=100
y=[]
for a in range(n):
	for i in range(n):
		rand=random.randint(1,100)
		if rand%2==0:
			y.append(True)
		else:
			y.append(False)
	matrix.append(y)
	y=[]


'''matrix=[[True, False, False], [False, True, True], [True, True, True]]
print matrix
n=3'''
def flow(matrix):
	'''this takes a matrix and returns a matrix of full sites that are connected with top row'''
	open_sites=[]
	temp_open=[]
	flag=True
	for a in range(n):
		if matrix[a][0]==True:
			temp_open.append("open")
		else:
			temp_open.append("close")
		flag=False
		for i in range(1,n):
			if matrix[a][i]==True:
				if i!=n-1:
					if matrix[a][i+1]==True and flag==False:
						temp_open.append("open")
						flag=True
					if matrix[a][i-1]==True and flag==False:
						temp_open.append("open")
						flag=True
				if i==n-1:
					if matrix[a][i-1]==True and flag==False:
						temp_open.append("open")
						flag=True
				
				if a!=0 and a!=(n-1) and flag==False:
					if matrix[a+1][i]==True:
						temp_open.append("open")
						flag=True
					if matrix[a-1][i]==True and flag==False:
						temp_open.append("open")
						flag=True
				if a==0:
					if matrix[a+1][i]==True:
						temp_open.append("open")
						flag=True
				if a==n-1:
					if matrix[a-1][i]==True and flag==False:
						temp_open.append("open")
						flag=True
				if flag==False:
					temp_open.append("close")
			else:
				temp_open.append("close")
			flag=False
		open_sites.append(temp_open)
		temp_open=[]
	return open_sites

def connected(matrix):
	'''checks if the matrix percolates'''
	a=flow(matrix)
	result=[]
	print a
	print matrix
	for i in range(n):
		result.append(a[i][n-1])
	if "open" in result:
		return True
	else:
		return False

print connected(matrix)
			





