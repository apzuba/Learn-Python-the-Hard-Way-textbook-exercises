import matplotlib.pyplot as plt
import numpy as np


# useful plot for disctete data, matches-like
x = np.linspace(0.1, 2 * np.pi, 20)
y = np.cos(x)

plt.stem(x, y, markerfmt='ro', use_line_collection=True)
plt.show()



# line events plot
events = np.array([1, 3, 5, 6, 8, 9, 10])

plt.eventplot(events, lineoffsets=0.5, linelengths=0.1)
plt.show()




# Density of plots, bee-haven like
x = np.random.randn(1000)
y = np.random.randn(1000)

plt.hexbin(x, y, gridsize=20, cmap='inferno')
plt.colorbar()
plt.show()



# 3D area values on a 2D plot
import matplotlib.tri as tri

x = np.array([0, 1, 0.5, 0.25])
y = np.array([0, 0, np.sqrt(3)/2, np.sqrt(3)/2])

triangles = np.array([[0, 1, 2], [1, 2, 3]])
values = np.array([1, 2])

triang = tri.Triangulation(x, y, triangles)
plt.tripcolor(triang, values, cmap='coolwarm')
plt.colorbar()
plt.show()



fs = 1000  # Sample rate (Hz)
t = np.arange(0, 10, 1/fs)  # Time vector
x = np.sin(2*np.pi*10*t) + np.random.randn(len(t))  # Signal with noise

plt.psd(x, Fs=fs)
plt.show()