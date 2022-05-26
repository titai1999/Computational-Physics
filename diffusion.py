import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation

Lx=1.0
Ly=1.0

tmax=1

k=1.0

n =100    # no of points along x and y direction

dx = Lx/(n - 1)
dy = Ly/(n - 1)

#dt=.0001
dt=.25*dx*dy/k  #for stability of the code

nt=int(tmax/dt)

x = np.linspace(0, Lx, n)
y = np.linspace(0, Ly, n)

X, Y = np.meshgrid(x,y)


def diffuse(nt,plottitle=None):
    udat=[]
    for i in range(nt + 1):
        
        un = u.copy()
        
        u[1:n-1, 1:n-1] = (un[1:n-1,1:n-1] + k*(dt / dx**2) * (un[1:n-1, 2:] - 2 * un[1:n-1, 1:n-1]+ un[1:n-1, 0:n-2])
                           + k*(dt / dy**2) * (un[2:,1: n-1] - 2 * un[1:n-1, 1:n-1] + un[0:n-2, 1:n-1]))
        udat.append(un.copy())

    udata=udat[::10]
    del(udat)       #deallocation of memory


    fig,ax=plt.subplots()
    plt.title(plottitle,fontsize=7)
    plt.xlabel("X")
    plt.ylabel("Y")
    d=ax.pcolormesh(X,Y,udata[1],cmap='magma',shading="auto")
    fig.colorbar(d)
    def animate(j):
        d.set_array(udata[j])
        return d
    anim=FuncAnimation(fig,animate,interval=1,frames=len(udata),repeat=False)
    plt.show()


#======================================================================================
    
# Part-1:
#only one side is at T=100(x=0) others are at T=0, interior temp. is 0

print("1st part: Change of T with time, for Initial condns. T(0,y)=100 degree, T(1,y)=T(x,0)=T(x,1)= 0 degree and interior temp. is zero.\n\n")

u = np.zeros((n, n))     #zero interior temperature

u[:,0]=100
#diffuse(nt,r"Change of T, for Initial condns. T(0,y)=$100\degree,\ T(1,y)=T(x,0)=T(x,1)= 0\degree$")


#======================================================================================

# Part-2:
#Two adjacent edges are at T=100(x=0 edge and y=0 edge) others two edges are at T=0, Interior temp. is random

print("2nd part: Change of T with time, for Initial condns. T(0,y)=T(x,0)=100 degree, T(1,y)=T(x,1)= 0 degree  and interior temp. is random")

u=60*np.random.rand(n,n)    #random interior temperature
u[:,0]=100
u[0,:]=100
u[:,n-1]=0
u[n-1,:]=0
diffuse(nt,r"Change of T, for Initial condns. T(0,y)=T(x,0)=$100\degree,\ T(1,y)=T(x,1)= 0\degree$ and interior temp. is random")
