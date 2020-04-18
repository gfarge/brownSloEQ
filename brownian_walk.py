	



""" --- Empty description --- """

# Imports

import numpy as np
import matplotlib.pyplot as plt


# Core
N = int(100)

dX = np.random.normal(1.,4.,N)
dY = np.random.normal(0.5,4.,N)
dr = np.random.normal(0.,1.,N)

X = np.cumsum(dX) - dX[0]
Y = np.cumsum(dY) - dY[0]
r = np.cumsum(dr) - dr[0]

fig, ax = plt.subplots(figsize=(8,3))
plt.axis('off')

ax.scatter(X,Y,c=r,s=abs(r*2)**2,cmap='plasma',marker='o',facecolor=None,zorder=10)

for ii in range(N-1):
	ax.plot((X[ii],X[ii+1]),(Y[ii],Y[ii+1]),c=plt.cm.inferno((r[ii+1]-r.min())/(r.max()-r.min())),lw=.5)

ax.text(0.5,0.,'A Brownian walk model\nfor slow-earthquakes',fontsize=20,transform=ax.transAxes,zorder=15)

plt.show()


