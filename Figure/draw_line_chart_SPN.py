import matplotlib.pyplot as plt
import numpy as np

# Example data
x = ['PCK@50', 'PCK@40', 'PCK@30', 'PCK@20']  # LaTeX formatted X-axis values

# Y-values for four different lines
y_values = [
    [86.89, 80.90, 69.85, 52.06],  # HPE + Stacked AE
    [86.63, 80.39, 68.74, 50.08],  # HPE + Traditional AE
    [85.66, 78.94, 66.67, 48.40],  # HPE + Mean Filter
    [78.39, 65.70, 47.90, 27.82],  # HPE + Gaussian Filter
    [71.66, 59.52, 43.69, 25.20],  # HPE
    [66.66, 44.52, 37.69, 10.20],  # Basic CNN
]


# Labels for each line
labels = ['HPE + Stacked AE', 'HPE + Traditional AE', 'HPE + Mean Filter', 'HPE + Gaussian Filter', 'HPE', "Basic CNN"]

# Set up the font properties for Computer Modern
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Computer Modern']

# Create a high-quality plot
plt.figure(figsize=(15, 10), dpi=100)  # High DPI for better quality

# Plot each line with specific styles
for i, y in enumerate(y_values):
    plt.plot(x, y, label=labels[i], linewidth=2, marker='o')  # Add markers for clarity

# Set title and labels without LaTeX formatting
plt.title('Performance Comparison of HPE Methods (SPN)', fontsize=18)
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
plt.savefig('SPN_line.png', format='pdf', bbox_inches='tight')
plt.rc('font', family='Arial')  # Change 'Arial' to a font you have installed

# Show the plot
plt.show()
