import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=Axes3D(fig)
x=[1,2,3,4,5,6,7,8,9]
y=[3,4,12,4,5,3,4,5,3]
z=[34,45,32,24,34,53,67,99,23]
ax.plot_surface(x,y,z,zdir='z',label='ys=0,zdir=z')
plt.show()