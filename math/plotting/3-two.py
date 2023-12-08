#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# plotting x ↦ y1 with a dashed red line
plt.plot(x, y1, color='red', linestyle='--', label='C-14')

# plotting x ↦ y2 with a solid green line
plt.plot(x, y2, color='green', linestyle='-', label='Ra-226')

# adding labels and title
plt.title("Exponential Decay of Radioactive Elements")
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")

# setting x-axis and y-axis ranges
plt.xlim(0, 20000)
plt.ylim(0, 1)

# adding legend in the upper right-hand corner
plt.legend()

# display the line graph
plt.show()
