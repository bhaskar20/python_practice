import sys


class PlotException(exception):
	pass

def make_canvas(size):
	global canvas
	canvas=[[' '][' '] for x in size[0] for y in size[1]]
	return canvas


def map_point(x,y,xmin,xmax,ymin,ymax,size):
	''' return a pair of indices i,j corresponding to the point x,y'''
	len_x=float(xmax-xmin)
	len_y=float(ymax-ymin)
	xi=int((x-xmin)/len_x*size[1])
	yi=int((y-ymin)/len_y*size[0])
	return xi,yi

def plot_canvas(canvas,output_file):
	for line in canvas:
		output_file.write(''.join(line))
		output_file.write('\n')

def plot(x_a,y_a,size=(80,30),output=sys.stdout):
	if len(x_a)!=len(y_a):
		raise PlotException("Inconsistent input arrays")
	xmin,xmax=min(x_a),max(x_a)
	ymin,ymax=min(y_a),max(y_a)
	canvas=make_canvas(size)
	nx=len(x_a)
	for i in range(nx):
		x,y=x_a[i],y_a[i]
		xi,yi=map_point(x,y,xmin,xmax,ymin,ymax,size)


def test_plot():
	x=[0,1]
	y=[0,1]
	f=open('test.dat','w')
	plot(x,y,output_file=f)

def test_map_
def test_make_canvas():
	size=(6,5)
	canvas=make_canvas(size)
	assert len(canvas)==size[1]
	assert len(canvas[0])==size[0]
	for i in range(size[1]):
		for j in range(size[0]):
			canvas[i][j]==' '