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
Z0 = 50.0  # system impedance (Ohm)

# =========================
# Load measured data
# =========================
data = pd.read_csv("3-3-1-unknown.csv")

f = data["Frequency(Hz)"].values
Z = data["|Z|"].values
phase = data["Theta"].values
Rs = data["Rs"].values
Xs = data["Xs"].values
RL = data["Return Loss(dB)"].values

# =========================
# Frequency where |Z| = Z0
# =========================
idx = np.argmin(np.abs(Z - Z0))

f_match = f[idx]
Rs_match = Rs[idx]
Xs_match = Xs[idx]
RL_match = RL[idx]

phase_match = phase[idx]

# =========================
# Identify component type
# =========================
if Xs_match > 0:
    component = "Inductor"
    value = Xs_match / (2 * np.pi * f_match)
    value_name = "L"
    unit = "H"
elif Xs_match < 0:
    component = "Capacitor"
    value = 1 / (2 * np.pi * f_match * abs(Xs_match))
    value_name = "C"
    unit = "F"
else:
    component = "Pure Resistor"
    value = Rs_match
    value_name = "R"
    unit = "Ohm"

# =========================
# Plot
# =========================
fig, ax = plt.subplots(figsize=(6.3, 3.5))

ax.plot(f, Z, linewidth=1, label="|Z|",c='black')
# ax.plot(f, Rs, linewidth=2, label="R_s", linestyle="--", c='black')
plt.xlim(f[0], f[-1])

ax.axhline(Z0, linestyle=":", linewidth=1.5, label="Z_0 = 50 $\Omega$", c='black')
ax.scatter(f_match, Z[idx], zorder=5, label="|Z| = Z_0", c='black')

ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Impedance |Z| ($\Omega$)")
# ax.set_title("Measured Impedance of Unknown Component")

ax.grid(True, linestyle=":", linewidth=0.8)
ax.legend()
fig.tight_layout()

# =========================
# Save figure as pickle
# =========================
with open("355.pkl", "wb") as f_pkl:
    pickle.dump(fig, f_pkl)

plt.show()

# =========================
# Print results
# =========================
print("Unknown component type:", component)
print(f"Frequency where |Z| = Z0: {f_match/1e6:.3f} MHz")
print(f"Series resistance Rs: {Rs_match:.2f} Ohm")
print(f"Return Loss: {RL_match:.2f} db")
print(f"{value_name} = {value:.3e} {unit}")
print(f"Phase at matching frequency: {phase_match:.2f} deg")

fig.savefig("355.pgf")

