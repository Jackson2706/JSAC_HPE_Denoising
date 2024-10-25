
import matplotlib.pyplot as plt
import numpy as np

# Example data
x_labels = [r'PCK$_{50}$', r'PCK$_{40}$', r'PCK$_{30}$', r'PCK$_{20}$']
x = np.arange(len(x_labels))  # Numerical positions for the bars

# Y-values for the six different methods
y_values = [
    [86.89, 80.90, 69.85, 52.06],  # HPE + Stacked AE
    [86.63, 80.39, 68.74, 50.08],  # HPE + Traditional AE
    [85.66, 78.94, 66.67, 48.40],  # HPE + Mean Filter
    [78.39, 65.70, 47.90, 27.82],  # HPE + Gaussian Filter
    [71.66, 59.52, 43.69, 25.20],  # HPE
    [66.66, 44.52, 37.69, 10.20],  # Basic CNN
]

labels = ['HPE + Stacked AE', 'HPE + Traditional AE', 'HPE + Mean Filter', 'HPE + Gaussian Filter', 'HPE', 'Basic CNN']

# Set up the plot
plt.style.use('seaborn-whitegrid')  # White background with grid
params = {
    "ytick.color": "black",
    "xtick.color": "black",
    "axes.labelcolor": "black",
    "axes.edgecolor": "black",
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Serif"]
}
plt.rcParams.update(params)

plt.figure(figsize=(10, 7), dpi=150)

bar_width = 0.15  # Width of bars

# Plot the bars for each method
for i, y in enumerate(y_values):
    plt.bar(x + i * bar_width, y, width=bar_width, label=labels[i])

# Configure the axes and labels
plt.ylabel('Percentage (\%)', fontsize=14)
plt.xticks(x + bar_width * 2.5, x_labels, fontsize=12)
plt.yticks(fontsize=12)

# Add legend with box
plt.legend(loc='upper right', fontsize=12, frameon=True, facecolor='white', edgecolor='black')  # Add box for legend

# Enable grid with black lines
plt.grid(visible=True, color='black', linestyle='--', alpha=0.7)  # Set grid lines to black

# Save and show the plot
plt.savefig('SPN_bar.png', format='png', bbox_inches='tight')
plt.show()
