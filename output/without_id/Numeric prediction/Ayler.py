import pandas as pnd
import matplotlib.pyplot as plt
import numpy as np


dt = 1
z_eps = 100
g = 9.81

def f(rocket_type, P):
    return np.array([P[3], P[4], P[5], 0, 0, -g])

def find_points(f, t0, P0, num_steps):
    solution = [(t0, P0)]
    t = t0
    P = P0

    for _ in range(num_steps):
        P = P + dt * f(0, P)
        t = t + dt

        solution.append((t, P))

    t = np.array([data_point[0] for data_point in solution])
    z = np.array([data_point[1][2] for data_point in solution])

    fig, ax = plt.subplots()
    ax.plot(t, z)
    plt.show()

find_points(f, 0, np.array([0, 0, 0, 2, 3, 100]), 50)