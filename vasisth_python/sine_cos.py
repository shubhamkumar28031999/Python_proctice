import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,2*np.pi,0.01)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,label='sine')
plt.plot(x,y2,label='cos')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("sine-cos")
plt.legend()
plt.show()