"""
Toy Missile Flight Simulation (SAFE & Educational)

This code simulates a fictional missile as a point mass with:
- Constant thrust for a limited burn time
- Gravity pulling it down
- Air drag opposing velocity

Dependencies: numpy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
dt = 0.05        # time step (s)
T = 60.0         # total sim time (s)
steps = int(T/dt)
times = np.linspace(0, T, steps)

# "Missile" parameters (fictional, arbitrary units)
mass = 50.0               # kg
thrust = 500.0            # N (constant during burn)
burn_time = 5.0           # seconds of thrust
drag_coeff = 0.1          # drag coefficient
area = 0.05               # m^2 cross-sectional area
rho = 1.2                 # air density (kg/m^3)
g = 9.81                  # gravity (m/s^2)

# Initial conditions
x, y = 0.0, 0.0          # position (m)
vx, vy = 100.0, 100.0    # initial velocity (m/s) - launch angle
trajectory_x, trajectory_y = [], []

for t in times:
    # Forces
    v = np.sqrt(vx**2 + vy**2)
    drag = 0.5 * rho * area * drag_coeff * v**2
    
    # Drag components opposite to velocity direction
    drag_x = -drag * (vx / v) if v > 0 else 0
    drag_y = -drag * (vy / v) if v > 0 else 0

    # Thrust (only while burning)
    if t < burn_time:
        thrust_x = thrust * (vx / v)
        thrust_y = thrust * (vy / v)
    else:
        thrust_x, thrust_y = 0, 0

    # Net accelerations
    ax = (thrust_x + drag_x) / mass
    ay = (thrust_y + drag_y) / mass - g

    # Update velocity
    vx += ax * dt
    vy += ay * dt

    # Update position
    x += vx * dt
    y += vy * dt
    if y < 0:   # stop if it hits the ground
        break

    trajectory_x.append(x)
    trajectory_y.append(y)

# Plot trajectory
plt.figure(figsize=(8,6))
plt.plot(trajectory_x, trajectory_y, label="Missile Path (fictional)")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Toy Missile Simulation (Safe & Educational)")
plt.grid(True)
plt.legend()
plt.show()
