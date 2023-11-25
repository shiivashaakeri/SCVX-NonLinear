# constraints.py
import numpy as np

def check_state_constraints(x):
    """
    Check if the state constraints are satisfied.

    State constraints:
    - pi/2 <= theta(t) <= pi/2
    - -7pi <= omega(t) <= 7pi

    Parameters:
    x (numpy array): The state vector at a given time, [theta, omega].

    Returns:
    bool: True if the state constraints are satisfied, False otherwise.
    """
    theta, omega = x
    return -np.pi/2 <= theta <= np.pi/2 and -7 * np.pi <= omega <= 7 * np.pi

def check_control_constraints(u):
    """
    Check if the control input constraints are satisfied.

    Control input constraints:
    0 <= u(t) <= 15

    Parameters:
    u (float): The control input at a given time.

    Returns:
    bool: True if the control input constraints are satisfied, False otherwise.
    """
    return 0 <= u <= 15

# Example usage in the optimization process
# if check_state_constraints(x_current) and check_control_constraints(u_current):
#     # Proceed with the optimization step
