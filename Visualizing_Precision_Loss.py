#import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Generate an array of values spaced logarithmically from 10^-50 to 10^50
x = np.logspace(-50, 50, 400)

# Define the precision_loss function to calculate the precision loss for very small and very large numbers
def precision_loss(x):
    return (np.log1p(np.exp(x)) - x - 1) / (x + 1)

# Calculate the precision loss for the generated values
y = precision_loss(x)

# Create a figure with a specified size
plt.figure(figsize=(14, 7))

# Plot the precision loss against the values
plt.plot(x, y, label='Precision Loss', color='b')

# Add title and labels to the plot
plt.title('Visualization of Precision Loss for Very Small and Very Large Numbers')
plt.xlabel('Value (Log Scale)')
plt.ylabel('Precision Loss')

# Set the x-axis to a logarithmic scale
plt.xscale('log')

# Add a legend to the plot
plt.legend()

# Add grid lines to the plot
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add annotations to highlight specific points on the plot
plt.annotate('Precision Loss for Large Numbers', xy=(10**30, 0.5), xytext=(10**25, 0.6),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Minimal Precision Loss for Small Numbers', xy=(10**-50, -0.3), xytext=(10**-30, -0.25),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Show the plot
plt.show()
