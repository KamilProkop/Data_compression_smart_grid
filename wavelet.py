import numpy as np
import pywt
import matplotlib.pyplot as plt

# Define the wavelet names
wavelets = ['haar', 'db2', 'coif1']

# Create a figure with a subplot for each wavelet
fig, axs = plt.subplots(len(wavelets), 1, figsize=(10, 6*len(wavelets)))

# Plot each wavelet
for i, wavelet in enumerate(wavelets):
   phi, psi, x = pywt.Wavelet(wavelet).wavefun(level=5)
   axs[i].plot(x, psi, label='psi')
   axs[i].plot(x, phi, label='phi', linestyle='--')
   axs[i].legend()
   axs[i].set_title(wavelet)

plt.tight_layout()
plt.show()
