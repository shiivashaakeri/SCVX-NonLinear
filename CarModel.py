import numpy as np
import scipy.linalg as la
from model import CarDynamics

class CarModel(CarDynamics):
    
    def __init__(self, dt, ix, iu, m=1.0):
        """
        Initialize the CarModel class with the time step, state dimension, 
        control dimension, and car mass.

        Parameters:
        dt (float): Time step for the discrete model.
        ix (int): State dimension.
        iu (int): Control dimension.
        m (float): Mass of the car, default is 1.0 unit.
        """
        super().__init__(m)
        self.deltT = dt

    def forward(self, x, u, discrete=True):
        """
        Compute the forward dynamics of the car model.

        Parameters:
        x (numpy array): Current state vector.
        u (numpy array): Current control input.
        discrete (bool): If True, use discrete dynamics. Otherwise, use continuous.

        Returns:
        numpy array: Next state vector.
        """
        N = len(x) if np.ndim(x) > 1 else 1  # Number of steps
        f = np.zeros_like(x)

        for i in range(N):
            if discrete:
                # Discrete dynamics using Euler integration
                f[i] = x[i] + self.deltT * self.state_derivative(x[i], u[i])
            else:
                # Continuous dynamics
                f[i] = self.state_derivative(x[i], u[i])

        return np.squeeze(f)
