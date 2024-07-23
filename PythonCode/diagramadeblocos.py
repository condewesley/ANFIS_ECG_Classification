import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 10))

# Remove axes
ax.axis('off')

# Define box properties
box_props = dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white')

# Define positions
positions = {
    "input": (0.1, 0.5),
    "Bd1": (0.25, 0.8),
    "Bd2": (0.25, 0.5),
    "Bd3": (0.25, 0.2),
    "sum1": (0.4, 0.8),
    "sum2": (0.4, 0.5),
    "sum3": (0.4, 0.2),
    "integrator1": (0.55, 0.8),
    "integrator2": (0.55, 0.5),
    "integrator3": (0.55, 0.2),
    "sum_output": (0.7, 0.5),
    "Cd": (0.85, 0.5),
    "output": (1.0, 0.5)
}

# Draw blocks
ax.text(*positions["input"], r'$u(t)$', ha='center', va='center', bbox=box_props)
ax.text(*positions["Bd1"], r'$B_{d1}$', ha='center', va='center', bbox=box_props)
ax.text(*positions["Bd2"], r'$B_{d2}$', ha='center', va='center', bbox=box_props)
ax.text(*positions["Bd3"], r'$B_{d3}$', ha='center', va='center', bbox=box_props)
ax.text(*positions["sum1"], r'$\Sigma$', ha='center', va='center', bbox=box_props)
ax.text(*positions["sum2"], r'$\Sigma$', ha='center', va='center', bbox=box_props)
ax.text(*positions["sum3"], r'$\Sigma$', ha='center', va='center', bbox=box_props)
ax.text(*positions["integrator1"], r'$\frac{1}{s + \lambda_1}$', ha='center', va='center', bbox=box_props)
ax.text(*positions["integrator2"], r'$\frac{1}{s + \lambda_2}$', ha='center', va='center', bbox=box_props)
ax.text(*positions["integrator3"], r'$\frac{1}{s + \lambda_3}$', ha='center', va='center', bbox=box_props)
ax.text(*positions["sum_output"], r'$\Sigma$', ha='center', va='center', bbox=box_props)
ax.text(*positions["Cd"], r'$C_d$', ha='center', va='center', bbox=box_props)
ax.text(*positions["output"], r'$y(t)$', ha='center', va='center', bbox=box_props)

# Draw arrows and connections
ax.annotate('', xy=(positions["Bd1"][0] - 0.05, positions["Bd1"][1]), xytext=(positions["input"][0] + 0.05, positions["input"][1]), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('', xy=(positions["Bd2"][0] - 0.05, positions["Bd2"][1]), xytext=(positions["input"][0] + 0.05, positions["input"][1]), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('', xy=(positions["Bd3"][0] - 0.05, positions["Bd3"][1]), xytext=(positions["input"][0] + 0.05, positions["input"][1]), arrowprops=dict(facecolor='black', shrink=0.05))

ax.annotate('', xy=(positions["sum1"][0] - 0.05, positions["sum1"][1]), xytext=(positions["Bd1"][0] + 0.05, positions["Bd1"][1]), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('', xy=(positions["sum2"][0] - 0.05, positions["sum2"][1]), xytext=(positions["Bd2"][0] + 0.05, positions["Bd2"][1]), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('', xy=(positions["sum3"][0] - 0.05, positions["sum3"][1]), xytext=(positions["Bd3"][0] + 0.05, positions["Bd3"][1]), arrowprops=dict(facecolor='black', shrink=0.05))

ax.annotate('', xy=(positions["integrator1"][0] - 0.05, positions["integrator1"][1]), xytext=(positions["sum1"][0] + 0.05, positions["sum1"][1]), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('', xy=(positions["integrator2"][0] - 0.05, positions["integrator2"][1]), xytext=(positions["sum2"][0] + 0.05, positions["sum2"][1]), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('', xy=(positions["integrator3"][0] - 0.05, positions["integrator3"][1]), xytext=(positions["sum3"][0] + 0.05, positions["sum3"][1]), arrowprops=dict(facecolor='black', shrink=0.05))

ax.annotate('', xy=(positions["sum_output"][0] - 0.05, positions["sum_output"][1]), xytext=(positions["integrator1"][0] + 0.05, positions["integrator1"][1]), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('', xy=(positions["sum_output"][0] - 0.05, positions["sum_output"][1]), xytext=(positions["integrator2"][0] + 0.05, positions["integrator2"][1]), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('', xy=(positions["sum_output"][0] - 0.05, positions["sum_output"][1]), xytext=(positions["integrator3"][0] + 0.05, positions["integrator3"][1]), arrowprops=dict(facecolor='black', shrink=0.05))

ax.annotate('', xy=(positions["Cd"][0] - 0.05, positions["Cd"][1]), xytext=(positions["sum_output"][0] + 0.05, positions["sum_output"][1]), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('', xy=(positions["output"][0] - 0.05, positions["output"][1]), xytext=(positions["Cd"][0] + 0.05, positions["Cd"][1]), arrowprops=dict(facecolor='black', shrink=0.05))

# Show plot
plt.show()
