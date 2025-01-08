import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_file(filename):
    df = pd.read_csv(filename)
    df["x"] = df["range"] * np.cos(np.pi*df["elevation"]/180)*np.sin(np.pi*df["azimuth"]/180)
    df["y"] = df["range"] * np.cos(np.pi * df["elevation"] / 180) * np.cos(np.pi * df["azimuth"] / 180)
    df["z"] = df["range"] * np.sin(np.pi * df["elevation"] / 180)
    return df


def separate_by_ids(table):
    grouped = table.groupby("ID")
    return [group for _, group in grouped]


def show_table(table, parameter1, parameter2):
    if type(parameter2) == list:
        for parameter in parameter2:
            plt.plot(table[parameter1], table[parameter])
    else:
        plt.plot(table[parameter1], table[parameter2])
    plt.show()


original_table = load_file(
    "input/with_id/With ID/Target point data/Tseelim_with_ID.csv")
tables = separate_by_ids(original_table)
for table in tables[150:153]:
    show_table(table, "time", ["x", "y", "z"])
