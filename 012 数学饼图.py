import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
mu,sigma=1000,200
a=np.random.normal(mu,sigma,size=1000)
plt.hist(a,20,density=1,histtype='stepfilled',facecolor='b',alpha=1)
plt.title('Histogram')
plt.show()


