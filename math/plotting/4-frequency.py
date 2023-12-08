#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# plotting a histogram of student scores
plt.hist(student_grades, bins=np.arange(0, 101, 10), edgecolor='black')

# adding labels and title
plt.title("Project A")
plt.xlabel("Grades")
plt.ylabel("Number of Students")

plt.xlim(0, 100)
plt.xticks(np.arange(0, 101, 10))
plt.ylim(0, 30)

# display the histogram
plt.show()
