# EnergyCost.py
import numpy as np

def calculate_energy_cost(u, weight_factor=1.0):
    """
    Calculate the energy cost for the control inputs.

    The energy cost is defined as the sum of the squares of the control inputs,
    weighted by a factor.

    Parameters:
    u (numpy array): The control input trajectory array.
    weight_factor (float): The weighting factor for the control input cost.

    Returns:
    float: The calculated energy cost value.
    """
    # Squaring the control inputs and applying the weight factor
    squared_control_inputs = np.square(u)
    weighted_squared_control_inputs = weight_factor * squared_control_inputs

    # Summing up the weighted control inputs to get the total energy cost
    total_energy_cost = np.sum(weighted_squared_control_inputs)

    return total_energy_cost

# Example usage
# u_trajectory = np.array([...])  # Control input trajectory
# energy_cost = calculate_energy_cost(u_trajectory, weight_factor=1.0)
