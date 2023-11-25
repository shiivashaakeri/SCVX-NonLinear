# Scaling.py
import numpy as np

class TrajectoryScaling:
    def __init__(self, x_min, x_max, u_min, u_max):
        """
        Initialize the TrajectoryScaling class with scaling parameters.

        Parameters:
        x_min (numpy array): Minimum values of the state variables for scaling.
        x_max (numpy array): Maximum values of the state variables for scaling.
        u_min (float): Minimum value of the control input for scaling.
        u_max (float): Maximum value of the control input for scaling.
        """
        self.x_min = x_min
        self.x_max = x_max
        self.u_min = u_min
        self.u_max = u_max

    def scale_state(self, x):
        """
        Scale a state vector based on the defined state bounds.

        Parameters:
        x (numpy array): The state vector to be scaled.

        Returns:
        numpy array: The scaled state vector.
        """
        return (x - self.x_min) / (self.x_max - self.x_min)

    def unscale_state(self, x_scaled):
        """
        Unscale a state vector to its original scale.

        Parameters:
        x_scaled (numpy array): The scaled state vector.

        Returns:
        numpy array: The original state vector.
        """
        return x_scaled * (self.x_max - self.x_min) + self.x_min

    def scale_control(self, u):
        """
        Scale a control input based on the defined control input bounds.

        Parameters:
        u (float): The control input to be scaled.

        Returns:
        float: The scaled control input.
        """
        return (u - self.u_min) / (self.u_max - self.u_min)

    def unscale_control(self, u_scaled):
        """
        Unscale a control input to its original scale.

        Parameters:
        u_scaled (float): The scaled control input.

        Returns:
        float: The original control input.
        """
        return u_scaled * (self.u_max - self.u_min) + self.u_min

# Example usage
# scaling = TrajectoryScaling(x_min=np.array([-np.pi/2, -7*np.pi]),
#                             x_max=np.array([np.pi/2, 7*np.pi]),
#                             u_min=0,
#                             u_max=15)
# x_scaled = scaling.scale_state(x_original)
# u_scaled = scaling.scale_control(u_original)
