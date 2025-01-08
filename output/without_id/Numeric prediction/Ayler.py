import pandas as pnd
import matplotlib.pyplot as plt
import numpy as np
from Model import *


dt = 1
z_eps = 0
g = 9.81


def f(rocket_type, P):
    return np.array([P[3], P[4], P[5], 0, 0, -g])


def find_hit_point(t0, P0, params):
    solution = [(t0, P0)]
    t = t0
    P = P0

    position = np.array(P[0:3])
    vel = np.array(P[3:6])
    x_arr = []
    y_arr = []
    t_arr = []
    cntr = 0
    while cntr < 30:
        acc = model(P, params)
        position = position + (2 * vel + dt*acc) / 2
        vel = vel + dt * acc
        P[0] = position[0]
        P[1] = position[1]
        P[2] = position[2]
        P[3] = vel[0]
        P[4] = vel[1]
        P[5] = vel[2]

        t = t + dt

        x_arr.append(P[0])
        t_arr.append(t)
        if P[2] < z_eps:
            break

        cntr += 1
    return [t_arr, x_arr]



