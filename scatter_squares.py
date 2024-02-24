"""Plotting and Styling Individual Points with scatter()"""

import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=20)
ax.set_ylabel("Value", fontsize=12)
ax.set_xlabel("Square of Value", fontsize=12)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()