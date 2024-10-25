import matplotlib.pyplot as plt
import numpy as np

# Example data
x_labels = ['PCK@50', 'PCK@40', 'PCK@30', 'PCK@20']  # X-axis labels
x = np.arange(len(x_labels))  # Numerical positions for the bars

# Y-values for the five different bars (representing different methods)
y_values = [
    [87.227, 81.344, 70.925, 53.699],  # HPE + Stacked AE
    [86.574, 79.382, 66.736, 45.768],  # HPE + Traditional AE
    [81.20, 71.50, 56.68, 35.03],      # HPE + Mean Filter
    [86.13,	79.01, 67.28, 47.66],      # HPE + Gaussian Filter
    [67.212, 53.728, 37.069, 19.675]   # HPE
]

# Labels for each method
labels = ['HPE + Stacked AE', 'HPE + Traditional AE', 'HPE + Mean Filter', 'HPE + Gaussian Filter', 'HPE']

# Set up the font properties for Computer Modern
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Computer Modern']

# Create a high-quality bar chart
plt.figure(figsize=(10, 7), dpi=150)  # High DPI for better quality

# Width of the bars and number of sets
bar_width = 0.15
bar_offsets = np.arange(len(y_values))  # To shift each bar group

# Plot each group of bars
for i, y in enumerate(y_values):
    plt.bar(x + i * bar_width, y, width=bar_width, label=labels[i])

# Set title and axis labels
plt.title('Performance Comparison of HPE Methods', fontsize=18)
plt.xlabel('PCK Thresholds', fontsize=14)
plt.ylabel('Percentage (%)', fontsize=14)

# Adjust the x-ticks to be in the center of the bar groups
plt.xticks(x + bar_width * 2, x_labels, fontsize=12)

# Fine-tune y-axis ticks
plt.yticks(fontsize=12)

# Add a legend and grid
plt.legend(loc='upper right', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Save the figure as a high-resolution PDF (vector format)
plt.savefig('research_plot_bar_chart.pdf', format='pdf', bbox_inches='tight')

# Show the plot
plt.show()
