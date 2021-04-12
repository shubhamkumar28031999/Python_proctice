import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,10000000)
y=np.cos(2*np.pi*x)
plt.grid() 
plt.plot(x,y,'g')
plt.xlabel("time")
plt.ylabel("voltage")
plt.title("graph")
plt.show()