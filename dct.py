import numpy as np
import matplotlib.pyplot as plt

# Define the size of the DCT matrix
N = 8

# Create a figure and subplots
fig, axes = plt.subplots(N, N, figsize=(8, 8))

# Loop through the basis functions and plot them
for i in range(N):
    for j in range(N):
        # Initialize an empty matrix to store the DCT basis function for this cell
        dct_matrix = np.zeros((N, N))

        # Compute the individual DCT basis function for this cell
        for x in range(N):
            for y in range(N):
                dct_matrix[x, y] = np.cos((2 * i + 1) * np.pi * x / (2 * N)) * np.cos((2 * j + 1) * np.pi * y / (2 * N))

        axes[i, j].imshow(dct_matrix, cmap='viridis', interpolation='nearest')
        axes[i, j].set_xticks([])
        axes[i, j].set_yticks([])

plt.show()
