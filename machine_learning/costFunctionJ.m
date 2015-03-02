function J = costFunctionJ(x,y,theta),
%x is the "design matrix" containing training examples
%y is the class labels

	m=size(x,1);
	predictions=x*theta;
	sqrErrors=(predictions-y).^2;
	J = 1/(2*m)*sum(sqrErrors); 