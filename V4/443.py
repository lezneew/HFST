import numpy as np

# sine_db = [10, -47.2, -64, -52.4, -54, -60.8]
# sine = []
# for db in sine_db:
#     lin = 10**(db/20)
#     sine.append(lin)
# print(sine)
#
# rel_sum = 0
# for c in sine[1:]:
#     print(c, c/sine[0])
#     rel_sum += (c/sine[0])**2
# print(rel_sum)
# thd = np.sqrt(rel_sum)


# sine_db = [10, -47.2, -64, -52.4, -54, -60.8]
# L_rel = []
# for db in sine_db:
#     L = db - 10
#     L_rel.append(L)
# print(f"hey{L_rel}")
#
# rel_sum = 0
# for c in L_rel[1:]:
#     lin = 10**(c/20)
#     print(f"{lin}")
#     rel_sum += (lin)**2
# print(rel_sum)



import math

# FFT levels in dB
sine_db = [10, -47.2, -64, -52.4, -56.4, -54, -60.8]

L1 = sine_db[0]          # fundamental level
harmonics = sine_db[1:] # higher harmonics

thd_sum = 0
for Ln in harmonics:
    L_rel = Ln - L1                 # relative dB
    Un_U1 = 10**(L_rel / 20)        # linear amplitude ratio
    thd_sum += Un_U1**2

THD = math.sqrt(thd_sum)

print("THD =", THD)
print("THD (%) =", THD * 100)






import pandas as pd
import matplotlib.pyplot as plt


# Load CSV file
data = pd.read_csv("sine434.csv")

# Create figure with specified size
plt.figure(figsize=(6.3, 3.5))

# Plot 1_x vs 1_y with thin black line
plt.plot(
    data["1_x"],          # frequency
    data["1_y"],          # amplitude
    color="black",
    linewidth=1
)

# Axis labels
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (dB)")

# Add grid
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Tight layout for LaTeX
plt.tight_layout()
plt.xlim(data["1_x"].iloc[0], data["1_x"].iloc[-1])

# Save as PGF
plt.show()
# Close figure
plt.close()
#
#
#
#
#
#
# # Load CSV files
# rect_data = pd.read_csv("rect434.csv")
# tri_data = pd.read_csv("tri434.csv")
# saw_data = pd.read_csv("saege434.csv")
#
# # Create figure with specified size
# plt.figure(figsize=(6.3, 3.5))
#
# # Plot each signal with specified color
# plt.plot(rect_data["1_x"], rect_data["1_y"], color="black", linewidth=1, label="Rectangular")
# plt.plot(tri_data["1_x"], tri_data["1_y"], color="red", linewidth=1, label="Triangle")
# plt.plot(saw_data["1_x"], saw_data["1_y"], color="green", linewidth=1, label="Sawtooth")
#
# # Axis labels
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Amplitude (dB)")
#
# # Add grid
# plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
#
# # Narrow x-axis limits to first and last frequency of the first dataset
# plt.xlim(rect_data["1_x"].iloc[0], rect_data["1_x"].iloc[-1])
#
# # Add legend
# plt.legend()
#
# # Tight layout for LaTeX
# plt.tight_layout()
#
# # Save as PGF
# plt.savefig("all_signals.pgf")
#
# # Close figure
# plt.close()
#
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
sine_data = pd.read_csv("sine434.csv")
rect_data = pd.read_csv("rect434.csv")
tri_data = pd.read_csv("tri434.csv")
saw_data = pd.read_csv("saege434.csv")

# Create 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(6.3, 3.5))  # width x height in inches

# Flatten axes for easy indexing
axes = axes.flatten()

# --- Plot sine wave ---
axes[0].plot(sine_data["1_x"], sine_data["1_y"], color="black", linewidth=1)
axes[0].set_title("Sine Wave")
axes[0].set_xlabel("Frequency (Hz)")
axes[0].set_ylabel("Amplitude (dB)")
axes[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[0].set_xlim(sine_data["1_x"].iloc[0], sine_data["1_x"].iloc[-1])

# --- Plot rectangular wave ---
axes[1].plot(rect_data["1_x"], rect_data["1_y"], color="black", linewidth=1)
axes[1].set_title("Rectangular Wave")
axes[1].set_xlabel("Frequency (Hz)")
axes[1].set_ylabel("Amplitude (dB)")
axes[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[1].set_xlim(rect_data["1_x"].iloc[0], rect_data["1_x"].iloc[-1])

# --- Plot triangle wave ---
axes[2].plot(tri_data["1_x"], tri_data["1_y"], color="black", linewidth=1)
axes[2].set_title("Triangle Wave")
axes[2].set_xlabel("Frequency (Hz)")
axes[2].set_ylabel("Amplitude (dB)")
axes[2].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[2].set_xlim(tri_data["1_x"].iloc[0], tri_data["1_x"].iloc[-1])

# --- Plot sawtooth wave ---
axes[3].plot(saw_data["1_x"], saw_data["1_y"], color="black", linewidth=1)
axes[3].set_title("Sawtooth Wave")
axes[3].set_xlabel("Frequency (Hz)")
axes[3].set_ylabel("Amplitude (dB)")
axes[3].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[3].set_xlim(saw_data["1_x"].iloc[0], saw_data["1_x"].iloc[-1])

# Adjust layout
plt.tight_layout()

# Save as PGF
plt.savefig("four_signals.pgf")

# Close figure
plt.close()




