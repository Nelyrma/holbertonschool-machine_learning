#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# bars' elements
people = ['Farrah', 'Fred', 'Felicia']
fruit_type = ['apples', 'bananas', 'oranges', 'peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

# position of bars on x-axis
x_pos = np.arange(len(people))

# width of bars
width = 0.5

for i in range(len(fruit)):
    plt.bar(x_pos, fruit[i], width, bottom=np.sum(fruit[:i], axis=0),
            color=colors[i], label=fruit_type[i])
    
# adding labels and title
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')

# x-axis and y-axis ranges 
plt.xticks(x_pos, people)
plt.yticks(np.arange(0, 90, 10))

# legend
plt.legend()

# display the stacked bar graph
plt.show()
