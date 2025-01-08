import numpy
import pandas as pnd
import matplotlib.pyplot as plt
import numpy as np
from Ayler import *
from Model import*



masses = [20, 160, 400, 670]


def predict_hit(table, rocket_type):
    mf = masses[rocket_type]
    # index = 200
    # x = table[index]["x"]
    # y = table[index]["y"]
    # z = table[index]["z"]
    # vx = (table[index + 1]["x"] - table[index - 1]["x"]) / 2
    # vy = (table[index + 1]["y"] - table[index - 1]["y"]) / 2
    # vz = (table[index + 1]["y"] - table[index - 1]["y"]) / 2
    # ax = (table[index + 1]["x"] - table[index]["x"]) - (table[index]["x"] - table[index - 1]["x"])
    # ay = (table[index + 1]["x"] - table[index]["x"]) - (table[index]["x"] - table[index - 1]["x"])
    # az = (table[index + 1]["x"] - table[index]["x"]) - (table[index]["x"] - table[index - 1]["x"])

    x = table["x"].values.tolist()
    y = table["y"].values.tolist()
    z = table["z"].values.tolist()
    vx = []
    vy = []
    vz = []
    t = table["time"].values.tolist()
    for i in range(len(x) - 2):
        vx.append((x[i+2] - x[i]) / (t[i+2] - t[i]))
        vy.append((y[i+2] - y[i]) / (t[i+2] - t[i]))
        vz.append((y[i+2] - y[i]) / (t[i+2] - t[i]))


    vx = numpy.array(vx)
    vy = numpy.array(vy)
    vz = numpy.array(vz)
    ax = []
    ay = []
    az = []
    for i in range(len(vx) - 2):
        ax.append((vx[i+2] - vx[i]) / (t[i+2] - t[i]))
        ay.append((vy[i + 2] - vy[i]) / (t[i + 2] - t[i]))
        az.append((vz[i + 2] - vz[i]) / (t[i + 2] - t[i]))

    x = x[2:-2]
    y = y[2:-2]
    z = z[2:-2]
    vx = vx[1:-1]
    vy = vy[1:-1]
    vz = vz[1:-1]


    model_params = fit_model(x, y, z, vx, vy, vz, ax, ay, az, mf)

    x = x[0]
    y = y[0]
    z = z[0]
    vx = vx[0]
    vy = vy[0]
    vz = vz[0]
    full_point = np.array([x, y, z, vx, vy, vz, mf])

    return find_hit_point(0, full_point, model_params)




