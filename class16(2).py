import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(loc=170, scale=10, size=250)

plt.hist(x)
plt.show()
