#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# plotting x ↦ y as a line graph
plt.plot(x, y, linestyle='-')

# adding labels and title
plt.title("Exponential Decay of C-14")
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")

# setting y-axis to logarithmic scale
plt.yscale('log')

# setting x-axis range from 0 to 28650
plt.xlim(0, 28650)

# display the line graph
plt.show()
