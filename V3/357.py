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
# Load matching network data
# =========================
data = pd.read_csv("3-3-2-longer_setup_shorted.csv")

f = data["Frequency(Hz)"].values
RL = data["Return Loss(dB)"].values
SWR = data["SWR"].values

# =========================
# Resonance frequency (minimum return loss)
# =========================
idx_res = np.argmin(RL)

f_res = f[idx_res]
RL_min = RL[idx_res]
SWR_res = SWR[idx_res]

# =========================
# Plot
# =========================
fig, ax = plt.subplots(figsize=(6.3, 3.5))

ax.plot(f, RL, linewidth=2, label="Return Loss (dB)")
ax.scatter(f_res, RL_min, zorder=5, label="Resonance")

ax.set_xlabel("Frequency (Hz)")
ax.set_xlabel("Return Loss (dB)")
ax.set_title("Measured Return Loss of Matching Network")

ax.grid(True, linestyle=":", linewidth=0.8)
ax.legend()
fig.tight_layout()

plt.show()
with open("357.pkl", "wb") as f_pkl:
    pickle.dump(fig, f_pkl)

# =========================
# Results
# =========================
print(f"Resonance frequency: {f_res/1e6:.3f} MHz")
print(f"Minimum return loss: {RL_min:.2f} dB")
print(f"SWR at resonance: {SWR_res}")
fig.savefig("357.pgf")
