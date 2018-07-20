import matplotlib.pyplot as plt
import numpy as np

N=20
theta=np.linspace(0,2*np.pi,N,endpoint=True)
radii=10*np.random.rand(N)
width=np.pi/4*np.random.rand(N)
ax=plt.subplot(111,projection='polar')
bars=ax.bar(theta,radii,width=width,bottom=0.0)


for r,bar in zip(radii,bars):
    bar.set_facecolor(plt.cm.viridis(r/10.0))
    bar.set_alpha(0.5)
    plt.show()


