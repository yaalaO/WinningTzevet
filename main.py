import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

EARTH_RADIUS = 6371000
ASHDOD = (31.77757586390034, 34.65751251836753)
KIRYAT_GAT = (31.602089287486198, 34.74535762921831)
OFAKIM = (31.302709659709315, 34.59685294800365)
TSEELIM = (31.20184656499955, 34.52669152933695)
MERON = (33.00023023451869, 35.404698698883585)
YABA = (30.653610411909529, 34.783379139342955)
MODIIN = (31.891980958022323, 34.99481765229601)
GOSH_DAN = (32.105913486777084, 34.78624983651992)
CARMEL = (32.65365306190331, 35.03028065430696)
ORIGIN = (29.490675, 34.902588)


def get_radar_xy(latlong):
    a = 6378137.0  # semi-major axis in meters
    f = 1 / 298.257223563  # flattening
    e2 = 2 * f - f ** 2  # eccentricity squared
    R = a  # in meters
    lat_rad = np.radians(latlong[0])
    lon_rad = np.radians(latlong[1])
    R_long = R / np.sqrt(1 - e2 * np.sin(lat_rad) ** 2)
    lat_ref = 0  # Reference latitude (equator)
    lon_ref = 0  # Reference longitude (prime meridian)
    delta_lat = lat_rad - np.radians(lat_ref)
    delta_lon = lon_rad - np.radians(lon_ref)
    x = R_long * delta_lon  # Longitude adjustment based on latitude
    y = R * delta_lat  # Latitude is constant
    return x, y


def load_file(filename, radar_ladlong):
    radar_x, radar_y = get_radar_xy(radar_ladlong)
    df = pd.read_csv(filename)
    df["time"] = df["time"] - np.min(df["time"])
    df["x"] = df["range"] * np.cos(np.pi*df["elevation"]/180)*np.sin(np.pi*df["azimuth"]/180) + radar_x
    df["y"] = df["range"] * np.cos(np.pi * df["elevation"] / 180) * np.cos(np.pi * df["azimuth"] / 180) + radar_y
    df["z"] = df["range"] * np.sin(np.pi * df["elevation"] / 180)
    df["dx/dt"] = df["x"].diff() / df["time"].diff()
    df["dy/dt"] = df["y"].diff() / df["time"].diff()
    df["dz/dt"] = df["z"].diff() / df["time"].diff()
    return df


def separate_by_ids(table):
    grouped = table.groupby("ID")
    return [group for _, group in grouped]


def show_table(table, parameter1, parameter2):
    if type(parameter2) == list:
        for parameter in parameter2:
            plt.scatter(table[parameter1], table[parameter])
    else:
        plt.scatter(table[parameter1], table[parameter2])
    plt.show()


def parabola(t, a, b, c):
    return a * t**2 + b * t + c


def linear(t, a, b):
    return a * t + b

if __name__ == "__main__":
    original_table = load_file(
        "input/with_id/With ID/Target bank data/Carmel_with_ID.csv", CARMEL)
    tables = separate_by_ids(original_table)
    for table in tables[0:20]:
        paramsz, _ = curve_fit(parabola, table['time'], table['z'])
        az, bz, cz = paramsz
        paramsx, _ = curve_fit(linear, table['time'], table['x'])
        ax, bx = paramsx
        paramsy, _ = curve_fit(linear, table['time'], table['y'])
        ay, by = paramsy
        plt.plot(table["time"], parabola(table["time"], az, bz, cz))
        plt.plot(table["time"], linear(table["time"], ax, bx))
        plt.plot(table["time"], linear(table["time"], ay, by))

        time_of_crash = (- bz + np.sqrt(bz**2 - 4*az*cz))
        x_crash = linear(time_of_crash, ax, bx)
        y_crash = linear(time_of_crash, ay, by)
        print(time_of_crash, x_crash, y_crash)

        show_table(table, "time", ["x", "y", "z"])
        # show_table(table, "time", ["dx/dt", "dy/dt", "dz/dt"])

