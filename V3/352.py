import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle


# =========================
# Load measurement data
# =========================
data = pd.read_csv("3-3-1-abs(Z)-Inductance.csv")

f = data["Frequency(Hz)"].values
Z = data["|Z|"].values
phase = data["Phase(deg)"].values

# =========================
# Inductance at 3.26 MHz
# =========================
f_target = 3.26e6
idx_L = np.argmin(np.abs(f - f_target))

L_326MHz = Z[idx_L] / (2 * np.pi * f[idx_L])

# =========================
# Phase when |Z| = 50 Ohm
# =========================
idx_50 = np.argmin(np.abs(Z - 50))
phase_at_50 = phase[idx_50]
f_at_50 = f[idx_50]

# =========================
# Self-resonant frequency (Z maximum)
# =========================
idx_maxZ = np.argmax(Z)
f_srf = f[idx_maxZ]

# Phase crossing zero (capacitive behavior starts)
idx_phase_neg = np.where(phase < 0)[0]
f_phase_neg = f[idx_phase_neg[0]] if len(idx_phase_neg) > 0 else None

# =========================
# Plot
# =========================
fig, ax1 = plt.subplots(figsize=(8, 5))

ax1.plot(f, Z, linewidth=2, label="|Z|", c='black')
ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("Impedance |Z| (Ω)")
ax1.grid(True, linestyle=":", linewidth=0.8)

ax2 = ax1.twinx()
ax2.plot(f, phase, linestyle="--", linewidth=2, label="Phase",c='black')
ax2.set_ylabel("Phase (deg)")

fig.suptitle("Measured Impedance and Phase of Inductor")

# Legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="best")

fig.tight_layout()
plt.show()

# =========================
# Print results
# =========================
print("Inductance at 3.26 MHz: {:.2e} H".format(L_326MHz))
print("Phase at |Z| = 50 Ω: {:.2f} deg at {:.2f} MHz".format(
    phase_at_50, f_at_50 / 1e6))
print("Self-resonant frequency (|Z| max): {:.2f} MHz".format(f_srf / 1e6))

if f_phase_neg:
    print("Phase becomes negative at: {:.2f} MHz".format(f_phase_neg / 1e6))

with open("352.pkl", "wb") as f:
    pickle.dump(fig, f)