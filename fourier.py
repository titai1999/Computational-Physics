
from math import*
import numpy as nmp
import matplotlib.pyplot as plt


def simpson(func,a,b,n=511):

	h=(b-a)/(n-1.0)

	y=nmp.zeros((n))

	x1=nmp.linspace(a,b,n)

	for i in range(0,n):

		x=x1[i] 
		y[i]=eval(func)

	s=0.0
	j=0
	while j<(n-1):
			
		if j%2.0==1:

			s+=4*y[j]

		else:
			s+=2*y[j]

		j=j+1

	s+=y[0]+y[n-1]
			
	intval=(h/3.0)*s

	return intval




def fourierseries(func,l1,l2,nc):


	a=nmp.zeros((nc))
	b=nmp.zeros((nc))

	l=(l2-l1)/2.0

	a[0]=(1/l)*simpson(func,l1,l2)
	for m in range(1,nc):

		fcos=func+'*cos('+str(m*pi/l)+'*x)'	#concatenation of f(x) and cos(m*pi x/l)

		fsin=func+'*sin('+str(m*pi/l)+'*x)'	#concatenation of f(x) and sin(m*pi x/l)

		a[m]=(1/l)*simpson(fcos,l1,l2)

		b[m]=(1/l)*simpson(fsin,l1,l2)

	

	np=1000		#no. of points for plotting

	x=nmp.linspace(l1,l2,np)
	y=nmp.zeros((np))

	for i in range(0,np):

		s=0.0

		for m in range(1,nc):

			s+=(a[m]*cos(m*pi*x[i]/l))+(b[m]*sin(m*pi*x[i]/l))

		y[i]=(0.5*a[0])+s

	
	plt.figure(1)

	plt.plot(x,y,'-')
	plt.savefig('Fourier.png')
	plt.show()

	plt.figure(2)

	plt.plot(nmp.arange(nc),a,'.')
	plt.savefig("Fouriercoeff.png")
	plt.show()

def f(x):
	if x>=-1.0 and x<-0.5:
		return 0.0
	if x>=-0.5 and x<0.5:
		return 1.0
	if x>=0.5 and x<=1.0:
		return 0.0

fourierseries('f(x)',-1.0,1.0,8)
