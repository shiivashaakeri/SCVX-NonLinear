# cost.py
import numpy as np

def calculate_cost(x, u, xf, R, Q):
    """
    Calculate the cost for the optimization problem.

    The cost is defined as:
    J = integral(u(t).T * R * u(t)) + (x(tf) - xf).T * Q * (x(tf) - xf)

    Parameters:
    x (numpy array): The state trajectory array.
    u (numpy array): The control input trajectory array.
    xf (numpy array): The desired final state.
    R (numpy array): The weight matrix for control input cost.
    Q (numpy array): The weight matrix for final state deviation cost.

    Returns:
    float: The calculated cost value.
    """

    # Calculate the control input cost
    control_cost = np.sum(np.dot(u.T, np.dot(R, u)))

    # Calculate the final state deviation cost
    final_state_deviation = x[-1] - xf
    final_state_cost = np.dot(final_state_deviation.T, np.dot(Q, final_state_deviation))

    return control_cost + final_state_cost

# Example usage
# xf = np.array([np.pi / 3, 5 * np.pi])  # Desired final state
# R = np.eye(1)  # Weight matrix for control input cost
# Q = np.eye(2)  # Weight matrix for final state deviation cost
# cost = calculate_cost(x_trajectory, u_trajectory, xf, R, Q)
