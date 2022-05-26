# The differential equations are soved using Euler's Method'

#variables are R_e, N, D

import numpy as np
import matplotlib.pyplot as plt

#Total population
N=1300000000.0

#threshold value of the epidemic
R_e=3.0

#duration of infection
D=14

#no. of days of observation
n=365

#susceptible individuals
S=[0.0]*n

#infected individuals
I=[0.0]*n

#removed individuals
R=[0.0]*n

#initial no. of infected individuals
I[0]=1.0

#initial no. of susceptible individuals
S[0]=N-I[0]

#initial no.of removed individuals
R[0]=0

#recovery rate
nu=1/D

#transmission rate
B=R_e*nu/S[0]

#interval in days
h=1.0

for t in range(n-1):
	S[t+1]=S[t]-(h*B*S[t]*I[t])
	I[t+1]=I[t]+h*I[t]*((B*S[t])-nu)
	R[t+1]=N-S[t+1]-I[t+1]

t=np.linspace(1,n,n)

plt.figure(1)

plt.plot(t,S,'-b',label='Susceptible population')
plt.plot(t,I,'-r',label='Infected population')
plt.plot(t,R,'-g',label='Removed population')

plt.xlabel('days')
plt.ylabel('size of different classes')

plt.legend()
plt.grid()

plt.savefig('SIR_Model.png')
plt.show()