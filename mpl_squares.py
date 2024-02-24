"""Plotting a simple line graph"""

# Import pyplot module using alias plt
import matplotlib.pyplot as plt


# Create a list called squares to hold data we will plot
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('Solarize_Light2')
# Common matplotlib convention by calling subplots()
# Subplots can generate one or more plots in the same figure
# fig represents the entire figure or collection of plots generated
# ax represents a single plot in the figure and is the commonly used variable
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# plt.show() opens Matplotlib's viewer and displays the plot
plt.show()
