import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5]
y=[23,35,56,23,50]

label=['one','two','three','four','five']
plt.bar(x,y,tick_label=label,width=0.6,color=['green','blue','red'])
plt.show()