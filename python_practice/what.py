def all_digits_even(n):
	''' Returns true if all digits in the number are even'''
	if n<0:n=-n
	while( n>0):
		if (n%2==1):return False
		n /=10
	return True
print all_digits_even(2445)

def least_perfect_square(n):
	i=1
	while (i*i<n):
		if (i*i==n):
			return i
		i+=1
	return i*i

print least_perfect_square(80)

def what( n ):
	i = 1
	while i * i < n:
		i += 1
	return i * i == n, i

print what(45)