#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


y = np.arange(0, 11) ** 3

# plotting y as a solid red line
plt.plot(y, color='red')

# range x-axis from 0 to 10
plt.xlim(0, 10)

# display the plot
plt.show()