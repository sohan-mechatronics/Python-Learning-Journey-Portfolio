import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 25, 30]

plt.plot(
    x,
    y,
    color="red",
    marker="o"
)

plt.title("Student Performance")

plt.xlabel("Test Number")

plt.ylabel("Marks")

plt.grid(True)

plt.show()