import matplotlib.pyplot as plt

# input = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# fig, ax = plt.subplots()

# plt.style.use('seaborn-v0_8')
# ax.plot(input, squares, linewidth=3)
# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)

# # Set size of tick labels.
# ax.tick_params(axis='both', labelsize=14)

# plt.show()

# using scatter plot to plot single point data
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Greens)

"""
A color map is a series of colors in a gradient that moves from one color to another.
"""
#Set char title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1100, 0, 1100000])

plt.show()
