import numpy as np
from scipy.optimize import minimize

g = 9.81


def model(inputs, params):
    """
    This model predicts the velocity given all of this data
    The model works only when the rocket is in free fall
    :param c: constant that should change from rocket to rocket
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


def cost_function(params, inputs, ax_obs, ay_obs, az_obs):
    """
    Computes the sum of squared errors for all three outputs.
    Inputs:
        params: Parameters to optimize.
        inputs: Tuple of independent variables (x1, x2, x3).
        ax_obs, ay_obs, az_obs: Observed accelerations.
    Output:
        Total error as a single value.
    """
    # Get model predictions
    y1_pred, y2_pred, y3_pred = model(inputs, params)

    # Compute errors for each output
    error1 = np.sum((y1_pred - ax_obs) ** 2)
    error2 = np.sum((y2_pred - ay_obs) ** 2)
    error3 = np.sum((y3_pred - az_obs) ** 2)

    # Total error (sum of all individual errors)
    total_error = error1 + error2 + error3
    print (total_error)
    return total_error


def fit_model(x, y, z, vx, vy, vz, ax, ay, az, mf):
    """
    This function fits the parameters to the data for one rocket
    and returns the best-fit parameters.
    :param x, y, z: Position data.
    :param vx, vy, vz: Velocity data.
    :param ax, ay, az: Observed acceleration data.
    :param mf: Final mass of the rocket.
    :return: The best-fit parameters (c, factor, b).
    """
    # Prepare the input data (same mass for all data points)
    mf = np.array([mf for _ in range(len(ax))])  # Assume `ax` has the same length as the other input data
    inputs_data = np.array([x, y, z, vx, vy, vz, mf])

    # Define the initial guess for the parameters [c, factor, b]
    initial_guess = np.array([0.01, 100, -5000])

    options = {
        'disp': True,        # Display optimization progress
        'maxiter': 10000,     # Set a higher maximum iteration limit
        'ftol': 1e-8,        # Set a tighter tolerance for convergence
        'xtol': 1e-8         # Tolerance for the solution of the parameters
    }

    # Perform the optimization
    result = minimize(cost_function, initial_guess,
                      args=(inputs_data, ax, ay, az),
                      method='BFGS',  # This is a popular quasi-Newton method
                      options=options)

    # Extract the best-fit parameters
    best_fit_params = result.x

    # Return the best-fit parameters
    return best_fit_params
