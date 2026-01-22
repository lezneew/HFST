import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Use PGF backend for LaTeX
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

# Load CSV files
rect_data = pd.read_csv("rect434.csv")
tri_data = pd.read_csv("437-rect.csv")

# Create figure with specified size
plt.figure(figsize=(6.3, 3))

# Plot each signal with specified color
plt.plot(rect_data["1_x"], rect_data["1_y"], color="black", linewidth=1, label="Rectangular")
plt.plot(tri_data["1_x"], tri_data["1_y"], color="red", linewidth=1, label="Modulated")

# Axis labels
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (dB)")

# Add grid
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Narrow x-axis limits to first and last frequency of the first dataset
plt.xlim(rect_data["1_x"].iloc[0], 3e6)

# Add legend
plt.legend()

# Tight layout for LaTeX
plt.tight_layout()

# Save as PGF
plt.savefig("445.pgf")

# Close figure
plt.close()
