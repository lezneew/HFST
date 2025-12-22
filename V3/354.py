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
Z = data["|Z|"].values

# =========================
# Resonance (minimum impedance)
# =========================
idx_min = np.argmin(Z)
f_res = f[idx_min]
Z_min = Z[idx_min]

# =========================
# Plot
# =========================
fig, ax = plt.subplots(figsize=(6.3, 3.5))

ax.plot(f, Z, linewidth=2, label="|Z| (Quartz)", c='black')
ax.scatter(f_res, Z_min, zorder=5, label="Resonance", c='black')

ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Impedance |Z| ($\Omega)")
ax.set_title("Measured Quartz Impedance vs Frequency")

ax.grid(True, linestyle=":", linewidth=0.8)
ax.legend()

fig.tight_layout()
plt.show()
with open("354.pkl", "wb") as f:
    pickle.dump(fig, f)
# =========================
# Print resonance info
# =========================
print(f"Resonance frequency: {f_res/1e6:.6f} MHz")
print(f"Minimum impedance: {Z_min:.2f} Ω")

fig.savefig("354.pgf")

