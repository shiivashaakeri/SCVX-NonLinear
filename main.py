# main.py

import numpy as np
from CarModel import CarModel
from Scvx import Scvx
from Scaling import TrajectoryScaling

# Define system parameters
ix = 2  # State dimension (theta, omega)
iu = 1  # Control dimension (torque)
tf = 100  # Final time in seconds
N = 1000  # Number of discretization steps
delT = tf / N  # Time step

# Initialize the car model and SCP solver
car_model = CarModel(delT, ix, iu)
scvx_solver = Scvx(ix, iu, N, delT)

# Define initial and final conditions for the car
xi = np.array([0, 0])  # Initial state: theta=0, omega=0
xf = np.array([np.pi / 3, 5 * np.pi])  # Final state: theta=pi/3, omega=5pi
u0 = np.array([0])  # Initial control input
uf = np.array([10])  # Final control input

# Define state and control limits
x_min = np.array([-np.pi/2, -7 * np.pi])
x_max = np.array([np.pi/2, 7 * np.pi])
u_min = np.array([0])
u_max = np.array([15])

# Initialize scaling
scaling = TrajectoryScaling(x_min, x_max, u_min, u_max)

# Define constraints for the optimization (placeholder)
constraints = {
    'type': 'ineq',
    'fun': lambda u: np.array([15 - np.abs(u_i) for u_i in u])  # Control input constraint
}

# Optimize the trajectory using SCP
optimized_x, optimized_u = scvx_solver.optimize_trajectory(xi, xf, u0, constraints)

# Plotting the results (Optional, requires matplotlib)
import matplotlib.pyplot as plt

time_steps = np.linspace(0, tf, N)



plt.plot(time_steps, optimized_u, label='Control Input (Torque)')
plt.title('Control Trajectory')
plt.xlabel('Time (s)')
plt.ylabel('Control Input')
plt.legend()

plt.tight_layout()
plt.show()
