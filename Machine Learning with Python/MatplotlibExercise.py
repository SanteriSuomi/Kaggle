import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 10, 100)
y = -0.5 * x ** 2 + 2 * x - 3

plt.plot(x, y, color="red", ls="-.", linewidth=2)

data_rnd_1 = np.random.rand(100, 2) * 100
data_rnd_2 = np.random.rand(120, 2) * 100

fig, ax = plt.subplots(2, figsize=(6, 9))
ax[0].scatter(data_rnd_1[:, 0:1], data_rnd_1[:, 1:2], c="green", marker="*")
ax[0].set_xlabel("dimension1", fontsize="10")
ax[0].set_ylabel("dimension2", fontsize="10")

ax[1].scatter(data_rnd_2[:, 0:1], data_rnd_2[:, 1:2], c="red", marker=".")
ax[1].set_xlabel("dimension1", fontsize="10")
ax[1].set_ylabel("dimension2", fontsize="10")

plt.show()
