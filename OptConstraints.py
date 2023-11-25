# OptConstraints.py
import numpy as np

class Constraints:
    def __init__(self, state_min, state_max, control_min, control_max):
        """
        Initialize the Constraints class with state and control input bounds.

        Parameters:
        state_min (numpy array): Minimum allowable values for the state.
        state_max (numpy array): Maximum allowable values for the state.
        control_min (float): Minimum allowable value for the control input.
        control_max (float): Maximum allowable value for the control input.
        """
        self.state_min = state_min
        self.state_max = state_max
        self.control_min = control_min
        self.control_max = control_max

    def check_state_constraints(self, x):
        """
        Check if the state constraints are satisfied.

        Parameters:
        x (numpy array): The state vector at a given time.

        Returns:
        bool: True if the state constraints are satisfied, False otherwise.
        """
        return np.all(x >= self.state_min) and np.all(x <= self.state_max)

    def check_control_constraints(self, u):
        """
        Check if the control input constraints are satisfied.

        Parameters:
        u (float): The control input at a given time.

        Returns:
        bool: True if the control input constraints are satisfied, False otherwise.
        """
        return self.control_min <= u <= self.control_max

# Example usage
# constraints = Constraints(state_min=np.array([-np.pi/2, -7*np.pi]),
#                           state_max=np.array([np.pi/2, 7*np.pi]),
#                           control_min=0,
#                           control_max=15)
# if constraints.check_state_constraints(x_current) and constraints.check_control_constraints(u_current):
#     # Proceed with the optimization step
