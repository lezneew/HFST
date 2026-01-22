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
sine_data1 = pd.read_csv("438-1.csv")
sine_data2 = pd.read_csv("438-2.csv")
sine_data3 = pd.read_csv("438-3.csv")
sine_data4 = pd.read_csv("438-4.csv")

sine_data1_200 = pd.read_csv("438-1-200khz.csv")
sine_data2_200 = pd.read_csv("438-2-200khz.csv")
sine_data3_200 = pd.read_csv("438-3-200khz.csv")
sine_data4_200 = pd.read_csv("438-4-200khz.csv")

# Create 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(6.3, 3.5))  # width x height in inches

# Flatten axes for easy indexing
axes = axes.flatten()

# --- Plot sine wave ---
axes[0].plot(sine_data1["1_x"], sine_data1["1_y"], color="black", linewidth=1)
axes[0].set_title("41,597 kHz")
axes[0].set_xlabel("Frequency (Hz)")
axes[0].set_ylabel("Amplitude (dB)")
axes[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[0].set_xlim(0.2e6, 0.8e6)

# --- Plot rectangular wave ---
axes[1].plot(sine_data2["1_x"], sine_data2["1_y"], color="black", linewidth=1)
axes[1].set_title("26,098 kHz")
axes[1].set_xlabel("Frequency (Hz)")
axes[1].set_ylabel("Amplitude (dB)")
axes[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[1].set_xlim(0.3e6, 0.7e6)

# --- Plot triangle wave ---
axes[2].plot(sine_data3["1_x"], sine_data3["1_y"], color="black", linewidth=1)
axes[2].set_title("19,472 kHz")
axes[2].set_xlabel("Frequency (Hz)")
axes[2].set_ylabel("Amplitude (dB)")
axes[2].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[2].set_xlim(0.3e6, 0.7e6)

# --- Plot sawtooth wave ---
axes[3].plot(sine_data4["1_x"], sine_data4["1_y"], color="black", linewidth=1)
axes[3].set_title("18,116 kHz")
axes[3].set_xlabel("Frequency (Hz)")
axes[3].set_ylabel("Amplitude (dB)")
axes[3].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[3].set_xlim(0.3e6, 0.7e6)
# Adjust layout
plt.tight_layout()

# Save as PGF
plt.savefig("446.pgf")

# Close figure
plt.close()

# Create 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(6.3, 3.5))  # width x height in inches

# Flatten axes for easy indexing
axes = axes.flatten()

# --- Plot sine wave ---
axes[0].plot(sine_data1_200["1_x"], sine_data1_200["1_y"], color="black", linewidth=1)
axes[0].set_title("41,597 kHz")
axes[0].set_xlabel("Frequency (Hz)")
axes[0].set_ylabel("Amplitude (dB)")
axes[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[0].set_xlim(sine_data1_200["1_x"].iloc[0], 0.5e6)

# --- Plot rectangular wave ---
axes[1].plot(sine_data2_200["1_x"], sine_data2_200["1_y"], color="black", linewidth=1)
axes[1].set_title("26,098 kHz")
axes[1].set_xlabel("Frequency (Hz)")
axes[1].set_ylabel("Amplitude (dB)")
axes[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[1].set_xlim(sine_data2_200["1_x"].iloc[0], 0.5e6)

# --- Plot triangle wave ---
axes[2].plot(sine_data3_200["1_x"], sine_data3_200["1_y"], color="black", linewidth=1)
axes[2].set_title("19,472 kHz")
axes[2].set_xlabel("Frequency (Hz)")
axes[2].set_ylabel("Amplitude (dB)")
axes[2].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[2].set_xlim(sine_data3_200["1_x"].iloc[0], 0.5e6)

# --- Plot sawtooth wave ---
axes[3].plot(sine_data4_200["1_x"], sine_data4_200["1_y"], color="black", linewidth=1)
axes[3].set_title("18,116 kHz")
axes[3].set_xlabel("Frequency (Hz)")
axes[3].set_ylabel("Amplitude (dB)")
axes[3].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[3].set_xlim(sine_data4_200["1_x"].iloc[0], 0.5e6)
# Adjust layout
plt.tight_layout()

# Save as PGF
plt.savefig("446-200.pgf")

# Close figure
plt.close()