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
sine_data25 = pd.read_csv("436-25kHz-sine.csv")
sine_data25_20p = pd.read_csv("436-25kHz-sine-20p.csv")
sine_data50 = pd.read_csv("436-50kHz-sine.csv")
sine_data50_20p = pd.read_csv("436-50kHz-sine-20p.csv")

# Create 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(6.3, 3.5))  # width x height in inches

# Flatten axes for easy indexing
axes = axes.flatten()

# --- Plot sine wave ---
axes[0].plot(sine_data50["1_x"], sine_data50["1_y"], color="black", linewidth=1)
axes[0].set_title("50 kHz, 70%")
axes[0].set_xlabel("Frequency (Hz)")
axes[0].set_ylabel("Amplitude (dB)")
axes[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[0].set_xlim(0.4e6, 0.6e6)

# --- Plot rectangular wave ---
axes[1].plot(sine_data50_20p["1_x"], sine_data50_20p["1_y"], color="black", linewidth=1)
axes[1].set_title("50 kHz, 20%")
axes[1].set_xlabel("Frequency (Hz)")
axes[1].set_ylabel("Amplitude (dB)")
axes[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[1].set_xlim(0.4e6, 0.6e6)

# --- Plot triangle wave ---
axes[2].plot(sine_data25["1_x"], sine_data25["1_y"], color="black", linewidth=1)
axes[2].set_title("25 kHz, 70%")
axes[2].set_xlabel("Frequency (Hz)")
axes[2].set_ylabel("Amplitude (dB)")
axes[2].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[2].set_xlim(0.4e6, 0.6e6)

# --- Plot sawtooth wave ---
axes[3].plot(sine_data25_20p["1_x"], sine_data25_20p["1_y"], color="black", linewidth=1)
axes[3].set_title("25 kHz, 20%")
axes[3].set_xlabel("Frequency (Hz)")
axes[3].set_ylabel("Amplitude (dB)")
axes[3].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[3].set_xlim(0.4e6, 0.6e6)
# Adjust layout
plt.tight_layout()

# Save as PGF
plt.savefig("444.pgf")

# Close figure
plt.close()