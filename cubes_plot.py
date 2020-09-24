import matplotlib.pyplot as plt

inputs = [1, 2, 3, 4, 5]
squares = [x**3 for x in inputs]
plt.plot(inputs, squares, linewidth = 4)

# Setting the title and label axes
plt.title("Cubes", fontsize = 20)
plt.xlabel("Values", fontsize = 16)
plt.ylabel("Cubed Numbers", fontsize = 16)

# Set size of tick labels.
plt.tick_params(axis = "both", labelsize = 14)

plt.show()
