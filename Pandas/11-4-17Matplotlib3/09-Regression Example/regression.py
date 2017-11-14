# Dependencies
from matplotlib import pyplot as plt
from scipy.stats import linregress
import numpy as np

x_axis = np.arange(0, 10, 1)
fake = [1, 2.5, 2.75, 4.25, 5.5, 6, 7.25, 8, 8.75, 9.8]

(slope, intercept, _, _, _) = linregress(x_axis, fake)
fit = slope * x_axis + intercept

plt.scatter(x_axis, fake, color='blue', marker='o')
plt.plot(x_axis, fit, color='blue', linestyle='dashed')

plt.title("Fake Banana Data")

plt.xlim(0, 10)
plt.ylim(0, 10)

plt.xlabel("Fake Banana Ages (in days)")
plt.ylabel("Fake Banana Weights (in Hundres of Kilograms)")

plt.show()
