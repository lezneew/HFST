import pickle

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("pgf")

matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

# =========================
# Load quartz measurement
# =========================
data = pd.read_csv("3-3-1-RL-quarz.csv")

f = data["Frequency(Hz)"].values
RL = data["Return Loss(dB)"].values
phase = data["Phase(deg)"].values

# =========================
# Resonance frequency
# =========================
idx_min = np.argmin(RL)
f0 = f[idx_min]
RL_min = RL[idx_min]

# =========================
# 3 dB bandwidth
# =========================
RL_3dB = -3#RL_min + 3

# Indices where RL is within 3 dB of minimum
indices = np.where(RL <= RL_3dB)[0]

f1 = f[indices[1]]
f2 = f[indices[-1]]
bandwidth = f2 - f1

# =========================
# Q factor
# =========================
Q = f0 / bandwidth

# =========================
# Plot
# =========================
fig, ax1 = plt.subplots(figsize=(6.3, 3.5))

# Return loss
ax1.plot(f, RL, linewidth=2, label="Return Loss (dB)", c='black')
ax1.axhline(RL_3dB, linestyle=":", linewidth=1.5, label="3 dB level", c='red')
# ax1.axvline(f0, linestyle="--", linewidth=1.5, label="Resonance frequency", c='red')

ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("Return Loss (dB)")
ax1.grid(True, linestyle=":", linewidth=0.8)

# Phase
ax2 = ax1.twinx()
ax2.plot(f, phase, linestyle="--", linewidth=2, label="Phase (deg)", c='black')
ax2.set_ylabel("Phase (deg)")

fig.suptitle("Measured Return Loss and Phase of Quartz Resonator")

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="right")

fig.tight_layout()
plt.show()

fig.savefig("353.pgf")

# =========================
# Results
# =========================
print(f"Resonance frequency f0: {f0/1e6:.6f} MHz")
print(f"3 dB bandwidth: {bandwidth:.2f} Hz {f1, f2}")
print(f"Quality factor Q: {Q:.2e}")
