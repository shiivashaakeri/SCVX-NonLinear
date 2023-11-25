# Scvx.py
import numpy as np
from scipy.optimize import minimize

class Scvx:
    def __init__(self, ix, iu, N, delT):
        """
        Initialize the Scvx class for Sequential Convex Programming.

        Parameters:
        ix (int): State dimension.
        iu (int): Control dimension.
        N (int): Number of discretization steps.
        delT (float): Time step for discretization.
        """
        self.ix = ix
        self.iu = iu
        self.N = N
        self.delT = delT

        # Initialize state and control trajectories
        self.x_traj = np.zeros((N, ix))
        self.u_traj = np.zeros((N, iu))

    def update_dynamics(self, x, u):
        """
        Update the dynamics based on the car model.

        Parameters:
        x (numpy array): The state trajectory array.
        u (numpy array): The control input trajectory array.

        Returns:
        numpy array: The updated state trajectory array.
        """
        # Ensure x is two-dimensional
        x = np.atleast_2d(x)
        new_x = np.zeros_like(x)

        for i in range(len(x) - 1):
            theta = x[i, 0]
            omega = x[i, 1]
            new_x[i + 1, 0] = x[i, 0] + self.delT * 0.5 * omega * theta
            new_x[i + 1, 1] = x[i, 1] + self.delT * u[i]

        return new_x

    def optimize_trajectory(self, xi, xf, u0, constraints):
        """
        Optimize the trajectory using SCP.

        Parameters:
        xi (numpy array): Initial state.
        xf (numpy array): Final desired state.
        u0 (numpy array): Initial control input guess.
        constraints (dict): Optimization constraints.

        Returns:
        Tuple[numpy array, numpy array]: Optimized state and control trajectories.
        """
        def objective(u_flat):
            u = u_flat.reshape((self.N, self.iu))
            x = self.update_dynamics(xi, u)
            # Define the cost function here. Placeholder for example.
            cost = np.sum(np.square(x - xf)) + np.sum(np.square(u - u0))
            return cost

        # Flatten the control trajectory for optimization
        u_flat_initial = self.u_traj.flatten()

        # Run the optimization
        result = minimize(objective, u_flat_initial, constraints=constraints, method='SLSQP')

        if result.success:
            optimized_u = result.x.reshape((self.N, self.iu))
            optimized_x = self.update_dynamics(xi, optimized_u)
            return optimized_x, optimized_u
        else:
            raise Exception("Optimization failed: " + result.message)

# Example usage
# scvx = Scvx(ix=2, iu=1, N=100, delT=0.1)
# xi = np.array([0, 0])  # Initial state
# xf = np.array([np.pi/3, 5*np.pi])  # Final desired state
# u0 = np.zeros(100)  # Initial control input guess
# constraints = {'type': 'ineq', 'fun': lambda u: ...}  # Define constraints here
# optimized_x, optimized_u = scvx.optimize_trajectory(xi, xf, u0, constraints)
