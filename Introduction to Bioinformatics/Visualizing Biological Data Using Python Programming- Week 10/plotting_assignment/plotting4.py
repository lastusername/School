import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

np.random.seed(3)
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

fig, ax = plt.subplots()
ax.step(x, y, linewidth=2.5)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
