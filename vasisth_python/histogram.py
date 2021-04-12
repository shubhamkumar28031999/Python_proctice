import matplotlib.pyplot as plt
import random
import numpy as np

#ages=[2,3,4,33,4,33,45,56,34,48,26,48,47,14,48,30,65,36,15,35,22,55,77,9,30,37,110,40,90,34,78]
ages=[random.randint(0,100)]
range=(0,100)
bins=10
plt.hist(ages,bins,range,histtype='bar',width=7)

plt.show()
