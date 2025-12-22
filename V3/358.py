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
fig, ax = plt.subplots(figsize=(6.3, 3.5))

ax.plot(f, RL, linewidth=2, label="Return Loss (dB)")
ax.scatter(f_res, RL_res, zorder=5, label="Resonance")

ax.set_xlabel("Frequency (Hz)")
ax.set_xlabel("Return Loss (dB)")
ax.set_title("Measured Return Loss of Matching Network")

ax.grid(True, linestyle=":", linewidth=0.8)
ax.legend()
fig.tight_layout()

plt.show()

# =========================
# Results
# =========================
print(f"Resonance frequency: {f_res/1e6:.3f} MHz")
print(f"Return loss at resonance: {RL_res:.2f} dB")
print(f"SWR at resonance: {SWR:.2f}")
print(f"Input impedance at resonance: {Z_in:.1f} Ohm")
fig.savefig("358.pgf")
