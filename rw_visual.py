"""Code to plot all the points of random walk"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()