import numpy as np

g = 9.81
def model(x, y, z, vx, vy, vz, c, mf):
    """
    This model predicts the velocity given all of this data
    The model works only when the rocket is in free fall
    :param c: constand that should change from rocket to rocket
    :param mf: final mass of the rocket
    :return: the acc in x, y, z
    """
    total_v = np.sqrt(vx**2 + vy**2 + vz**2)
    drag_force = c * np.exp(-z/10.4) * total_v**2

    v_part_x = vx / total_v
    v_part_y = vy / total_v
    v_part_z = vz / total_v


    f_x = drag_force * v_part_x
    f_y = drag_force * v_part_y
    f_z = drag_force * v_part_z - (mf * g)

    a_x = f_x / mf
    a_y = f_y / mf
    a_z = f_z / mf
    return a_x, a_y, a_z