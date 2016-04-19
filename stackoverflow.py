from scipy.stats import chi2
import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize
import pickle

objects = []
with open("priceZZZ", "rb") as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break
for i in range(len(objects)):
    plt.plot(np.linspace(0, len(objects[i][0]), len(objects[i][0])), objects[i][0], label=i)
plt.legend()
plt.show()