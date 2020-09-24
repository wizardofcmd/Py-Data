import matplotlib.pyplot as plt

# Generating a list of x values from 1 all the way to 5000 and storing them
x_values = list(range(1, 5001))
# Looping through all the values in the list and cubing each number
y_values = [x**3 for x in x_values]

# Plotting all points on the chart
# C taking y_values as an argument, allowing the colormap to color the
# lowest numbers in the set and gradually darken as it gets higher
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.twilight, edgecolor = "none", s = 10)

# Setting the chart title and labelling axes
plt.title("Cubes to 5000")
plt.xlabel("Values")
plt.ylabel("Cubed")

# Setting the x and y axes range
plt.axis([1, 5000, 1, 125000000000])

plt.show()
