import numpy as np
from scipy.optimize import minimize

g = 9.81


def model(inputs, params):
    """
    This model predicts the velocity given all of this data
    The model works only when the rocket is in free fall
    :param c: constand that should change from rocket to rocket
    :param mf: final mass of the rocket
    :return: the acc in x, y, z
    """
    x, y, z, vx, vy, vz, mf = inputs
    c, factor, b = params
    total_v = np.sqrt(vx ** 2 + vy ** 2 + vz ** 2)
    drag_force = c * np.exp(-(z + b) / factor) * total_v ** 2

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


def cost_function(params, inputs, y1_obs, y2_obs, y3_obs):
    """
    Computes the sum of squared errors for all three outputs.
    Inputs:
        params: Parameters to optimize.
        inputs: Tuple of independent variables (x1, x2, x3).
        y1_obs, y2_obs, y3_obs: Observed outputs.
    Output:
        Total error as a single value.
    """
    # Get model predictions
    y1_pred, y2_pred, y3_pred = model(inputs, params)

    # Compute errors for each output
    error1 = np.sum((y1_pred - y1_obs) ** 2)
    error2 = np.sum((y2_pred - y2_obs) ** 2)
    error3 = np.sum((y3_pred - y3_obs) ** 2)

    # Total error (sum of all individual errors)
    total_error = error1 + error2 + error3
    return total_error


def fit_model(x, y, z, vx, vy, vz, ax, ay, az, mf):
    """
    THis funcntion gets the flight data for one rocket miltiple times and
    fits the c parameter to it
    :return: the fitest c
    the input is a list of data sets
    mf is a an intger that is the final mass of the rocket
    """

    inputs_data = np.array([x, y, z, vx, vy, vz, mf])
    initial_guess = np.array([1, 10.4, 1000])  # c, factor, off_in_z

    # Perform the optimization
    result = minimize(cost_function, initial_guess,
                      args=(inputs_data, ax, ay, az))

    # Extract the best-fit parameters
    best_fit_params = result.x

    # Print the results
    print("Optimization successful:", result.success)
    print("Best-fit parameters:", best_fit_params)


