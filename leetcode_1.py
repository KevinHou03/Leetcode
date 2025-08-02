# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         memo = {}
#         for i in range(len(nums)):
#             if target - nums[i] in memo:
#                 return [memo[target - nums[i]], i]
#             memo[nums[i]] = i
#         return []

#
import numpy as np
import matplotlib.pyplot as plt

# Define time values
t_values = np.linspace(0, 2, 20)  # Time range from 0 to 2

# Define initial x values
x0_values = np.linspace(-5, 5, 20)  # Various initial x positions

plt.figure(figsize=(8, 6))

# Plot characteristic lines: x = x0 ± 3t
for x0 in x0_values:
    plt.plot(x0 + 3 * t_values, t_values, 'blue', lw=1)  # Right-moving characteristics
    plt.plot(x0 - 3 * t_values, t_values, 'red', lw=1)  # Left-moving characteristics

# Highlight the region where g(x) is nonzero (-1 < x < 1)
plt.axvline(x=-1, color='green', linestyle='--', label=r"$x = -1$")
plt.axvline(x=1, color='green', linestyle='--', label=r"$x = 1$")

# Labels and title
plt.xlabel("x")
plt.ylabel("t")
plt.legend()
plt.grid(True)# aaaaaaaa

# Show the plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Define parameters
# L = np.pi  # Spatial domain [0, pi]
# T = 5       # Total time
# Nx = 50     # Number of spatial points
# Nt = 200    # Number of time steps
#
# dx = L / (Nx - 1)  # Spatial step size
# dt = T / Nt        # Time step size
# c = 1              # Wave speed
#
# # Stability condition (CFL condition)
# s = (c * dt / dx) ** 2  # Courant umber
# if s > 1:
#     raise ValueError("Stability condition violated: Reduce dt or increase dx.")
#
# # Initialize solution arrays
# u = np.zeros((Nt, Nx))  # u(t, x)
#
# # Initial condition u(0, x) = 1 for all x
# u[0, :] = 1
#
# # First time step using initial velocity condition u_t(0, x) = 0
# for i in range(1, Nx - 1):
#     u[1, i] = u[0, i] + 0.5 * s * (u[0, i+1] - 2 * u[0, i] + u[0, i-1])
#
# # Time stepping loop
# for n in range(1, Nt - 1):
#     for i in range(1, Nx - 1):
#         u[n+1, i] = 2 * u[n, i] - u[n-1, i] + s * (u[n, i+1] - 2 * u[n, i] + u[n, i-1])
#
# # Plot the results
# x = np.linspace(0, L, Nx)
# time_steps = [0, int(Nt/4), int(Nt/2), Nt-1]  # Select times to plot
# plt.figure(figsize=(10, 6))
#
# for t in time_steps:
#     plt.plot(x, u[t, :], label=f't = {t * dt:.2f}')
#
# plt.xlabel('x')
# plt.ylabel('u(t, x)')
# plt.title('Numerical Solution of the Wave Equation')
# plt.legend()
# plt.grid()
# plt.show()
#
# # Print the numerical solution for selected time steps
# for t in time_steps:
#     print(f'Solution at t = {t * dt:.2f}:')
#     print(u[t, :])
