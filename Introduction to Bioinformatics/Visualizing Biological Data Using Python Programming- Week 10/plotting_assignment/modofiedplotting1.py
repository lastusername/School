from matplotlib import pyplot as plt

y = [10, 5, 8, 4, 2]
plt.plot(y, color='orange', linestyle='dotted', linewidth=3)
plt.title("Updated Line Plot")
plt.xlabel("Custom X-axis")
plt.ylabel("Custom Y-axis")
plt.grid(True)
plt.show()

# I modified Code 1 by changing the line color to orange, using a dotted line style, adding a title and axis labels, and turning on the grid.