import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
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
c = 3e8           # speed of light (m/s)
VF = 0.66         # RG-58 velocity factor
v = VF * c

# =========================
# Load data
# =========================
cable1 = pd.read_csv("3-3-2-shorter.csv")
cable2 = pd.read_csv("3-3-2-longer.csv")

f1 = cable1["Frequency(Hz)"].values
p1 = cable1["Phase(deg)"].values

f2 = cable2["Frequency(Hz)"].values
p2 = cable2["Phase(deg)"].values

# =========================
# Linear fits (phase vs frequency)
# =========================
coef1 = np.polyfit(f1, p1, 1)
coef2 = np.polyfit(f2, p2, 1)

slope1 = coef1[0]  # deg/Hz
slope2 = coef2[0]

# =========================
# Delays and lengths
# =========================
tau1 = -slope1 / 360
tau2 = -slope2 / 360

L1 = v * tau1 / 2
L2 = v * tau2 / 2

# =========================
# Plot
# =========================
fig, ax = plt.subplots(figsize=(6.3, 3.5))

ax.plot(f1, p1, linewidth=1, c='black', label="Cable 1 – Measured phase")
# ax.plot(f1, np.polyval(coef1, f1), "--", linewidth=2, label="Cable 1 – Fit")

ax.plot(f2, p2, "--", linewidth=1, c='black', label="Cable 2 – Measured phase")
# ax.plot(f2, np.polyval(coef2, f2), "--", linewidth=2, label="Cable 2 – Fit")
plt.xlim(f1[0], f1[-1])

ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Phase of Return Loss (deg)")
# ax.set_title("Phase of Return Loss vs Frequency")

ax.grid(True, linestyle=":", linewidth=0.8)
ax.legend(loc="right")
fig.tight_layout()

# =========================
# Save figure as pickle
# =========================
with open("return_loss_phase_cable_lengths.pkl", "wb") as f:
    pickle.dump(fig, f)

plt.show()
with open("356.pkl", "wb") as f_pkl:
    pickle.dump(fig, f_pkl)

# =========================
# Results
# =========================
print("Cable 1 length: {:.3f} m".format(L1))
print("Cable 2 length: {:.3f} m".format(L2))
print("Total cable length: {:.3f} m".format(L1 + L2))
fig.savefig("356.pgf")
