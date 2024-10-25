import matplotlib.pyplot as plt
import numpy as np

# Example data
x_labels = [r'PCK$_{50}$', r'PCK$_{40}$', r'PCK$_{30}$', r'PCK$_{20}$']
x = np.arange(len(x_labels))  # Numerical positions for the bars

# Y-values for the six different methods
y_values = [
    [87.227, 81.344, 70.925, 53.699],  # HPE + Stacked AE
    [86.574, 79.382, 66.736, 45.768],  # HPE + Traditional AE
    [81.20, 71.50, 56.68, 35.03],      # HPE + Mean Filter
    [86.13, 79.01, 67.28, 47.66],      # HPE + Gaussian Filter
    [67.212, 53.728, 37.069, 19.675],  # HPE
    [52.21, 48.73, 22.07, 5.68],       # Basic CNN
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
plt.savefig('AWGN_bar.png', format='png', bbox_inches='tight')
plt.show()
