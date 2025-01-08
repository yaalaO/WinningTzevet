import pandas as pd
import numpy as np

def classfy_from_index(l, x):
    """
    this fucntion gets in index x and finds all of the point that are in the line with x
    :param l: should be a list of x, y, z, t
    """
    eps = 5000
    points = [l[x]]
    while x < l.size:

        curr = x + 1
        min_ind = -1
        min_val = eps
        while curr < l.size and l[curr][3] - l[x][3] <= 5:
            curr_dist = culc_dist(l[x], l[curr])
            if curr_dist < min_val:
                min_val = curr_dist
                min_ind = curr
            curr += 1

        if min_val >= eps:
            break
        points.append(l[curr])
        x = curr

    return points


def load_file(filename):
    df = pd.read_csv(filename)
    df["x"] = df["range"] * np.cos(np.pi*df["elevation"]/180)*np.sin(np.pi*df["azimuth"]/180)
    df["y"] = df["range"] * np.cos(np.pi * df["elevation"] / 180) * np.cos(np.pi * df["azimuth"] / 180)
    df["z"] = df["range"] * np.sin(np.pi * df["elevation"] / 180)
    return df

def separate_by_ids(table):
    grouped = table.groupby("ID")
    return [group for _, group in grouped]

def culc_dist(p1, p2):
    # culc the dist between two x, y, z, t points
    d = (p1[0] - p2[0]) ** 2
    d += (p1[1] - p2[1]) ** 2
    d += (p1[2] - p2[2]) ** 2
    d += (p1[3] - p2[3]) ** 2
    d = np.sqrt(d)
    return d

a = load_file("input/with_id/With ID/Impact points data/Ashdod_with_ID.csv")
a= separate_by_ids(a)[0]
a = a[["x", "y", "z", "time"]]
a = a.to_numpy()

print (len(a))
a = classfy_from_index(a, 0)
print (len(a))
