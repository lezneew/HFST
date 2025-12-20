import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================
# Constants
# =========================
Z0 = 50.0  # system impedance (Ohm)

# =========================
# Load antenna data
# =========================
data = pd.read_csv("3-3-3-antenna-better.csv")

f = data["Frequency(Hz)"].values
RL = data["Return Loss(dB)"].values

# =========================
# Resonance frequency
# =========================
idx_res = np.argmin(RL)
f_res = f[idx_res]
RL_res = RL[idx_res]

# =========================
# SWR calculation
# =========================
Gamma = 10 ** (-RL_res / 20)
SWR = (1 + Gamma) / (1 - Gamma)

# =========================
# Input impedance at resonance
# =========================
Z_in = Z0 * (1 + Gamma) / (1 - Gamma)

# =========================
# Plot
# =========================
plt.figure(figsize=(8, 5))

plt.plot(f, RL, linewidth=2, label="Return Loss (dB)")
plt.scatter(f_res, RL_res, zorder=5, label="Resonance")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Return Loss (dB)")
plt.title("Measured Return Loss of Antenna")

plt.grid(True, linestyle=":", linewidth=0.8)
plt.legend()
plt.tight_layout()
plt.show()

# =========================
# Results
# =========================
print(f"Resonance frequency: {f_res/1e6:.3f} MHz")
print(f"Return loss at resonance: {RL_res:.2f} dB")
print(f"SWR at resonance: {SWR:.2f}")
print(f"Input impedance at resonance: {Z_in:.1f} Ohm")
