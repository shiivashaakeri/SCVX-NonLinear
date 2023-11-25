# savefunction.py
import numpy as np

def save_results(filename, x_trajectory, u_trajectory):
    """
    Save the optimized state and control trajectories to a file.

    Parameters:
    filename (str): The name of the file where the results will be saved.
    x_trajectory (numpy array): The optimized state trajectory array.
    u_trajectory (numpy array): The optimized control input trajectory array.
    """
    with open(filename, 'w') as file:
        file.write("State Trajectory (Theta, Omega):\n")
        np.savetxt(file, x_trajectory, fmt='%.6f', header='Theta, Omega')

        file.write("\nControl Input Trajectory (Torque):\n")
        np.savetxt(file, u_trajectory, fmt='%.6f', header='Torque')

# Example usage
# save_results('optimization_results.txt', optimized_x, optimized_u)
