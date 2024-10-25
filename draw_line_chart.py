import matplotlib.pyplot as plt
import numpy as np

# Example data
x = ['PCK@50', 'PCK@40', 'PCK@30', 'PCK@20']  # LaTeX formatted X-axis values

# Y-values for four different lines
y_values = [
    [87.227, 81.344, 70.925, 53.699],  # HPE + Stacked AE
    [86.574, 79.382, 66.736, 45.768],  # HPE + Traditional AE
    [81.20, 71.50, 56.68, 35.03],      # HPE + Mean Filter
    [86.13,	79.01, 67.28, 47.66],
    [67.212, 53.728, 37.069, 19.675]   # HPE
]

# Labels for each line
labels = ['HPE + Stacked AE', 'HPE + Traditional AE', 'HPE + Mean Filter', 'HPE + Gaussian Filter', 'HPE']

# Set up the font properties for Computer Modern
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Computer Modern']

# Create a high-quality plot
plt.figure(figsize=(10, 7), dpi=150)  # High DPI for better quality

# Plot each line with specific styles
for i, y in enumerate(y_values):
    plt.plot(x, y, label=labels[i], linewidth=2, marker='o')  # Add markers for clarity

# Set title and labels without LaTeX formatting
plt.title('Performance Comparison of HPE Methods', fontsize=18)
plt.xlabel('PCK Thresholds', fontsize=14)
plt.ylabel('Percentage (%)', fontsize=14)

# Fine-tune tick parameters
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add legend with a proper location
plt.legend(loc='upper right', fontsize=12)

# Add a grid for clarity
plt.grid(True, linestyle='--', alpha=0.7)

# Save the figure as a high-resolution PDF (vector format)
plt.savefig('research_plot.png', format='pdf', bbox_inches='tight')
plt.rc('font', family='Arial')  # Change 'Arial' to a font you have installed

# Show the plot
plt.show()
