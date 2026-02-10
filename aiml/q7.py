import matplotlib.pyplot as plt
sales = [120, 135, 150, 160, 145, 170, 180, 175, 160, 155, 140, 130]
months = list(range(1, 13))
plt.hist(sales, bins=5, label="Sales Frequency")
plt.xlabel("Sales Range")
plt.ylabel("Frequency")
plt.title("Sales Histogram")
plt.legend(loc="upper right")
plt.show()
