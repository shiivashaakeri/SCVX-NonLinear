# model.py
import numpy as np

class CarDynamics:
    def __init__(self, m=1.0):
        """
        Initialize the car dynamics model.

        Parameters:
        m (float): The mass of the car, default is 1.0 unit.
        """
        self.m = m  # Mass of the car

    def state_derivative(self, x, u):
        """
        Compute the derivative of the state.

        State vector x = [theta, omega]^T
        Control input u is the torque.

        Parameters:
        x (numpy array): The current state vector [theta, omega].
        u (float): The current control input (torque).

        Returns:
        numpy array: The derivative of the state vector.
        """
        theta, omega = x
        theta_dot = 0.5 * omega * theta  # d(theta)/dt
        omega_dot = u / self.m  # d(omega)/dt

        return np.array([theta_dot, omega_dot])

    def update_state(self, x, u, dt):
        """
        Update the state based on the current state, control input, and time step.

        Parameters:
        x (numpy array): The current state vector [theta, omega].
        u (float): The current control input (torque).
        dt (float): The time step for the update.

        Returns:
        numpy array: The updated state vector.
        """
        x_dot = self.state_derivative(x, u)
        x_new = x + dt * x_dot  # Euler integration for state update

        return x_new

# Example usage
# car_model = CarDynamics(m=1.0)
# x_current = np.array([theta_value, omega_value])
# u_current = torque_value
# dt = time_step
# x_next = car_model.update_state(x_current, u_current, dt)
