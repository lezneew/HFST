import pandas as pd
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
# CSV-Dateien einlesen
# =========================
carbon = pd.read_csv("3-3-1-RL-kohle.csv")
coax = pd.read_csv("3-3-1-RL-terminator.csv")

# Frequenz
f_carbon = carbon["Frequency(Hz)"]
f_coax = coax["Frequency(Hz)"]

# Widerstand und Impedanz
Rs_carbon = carbon["Rs"]
Z_carbon = carbon["|Z|"]

Rs_coax = coax["Rs"]
Z_coax = coax["|Z|"]

# =========================
# Plot
# =========================
fig, ax = plt.subplots(figsize=(6.3, 3.5))

# Carbon resistor
ax.plot(f_carbon, Rs_carbon,
        label="Rs – Carbon resistor",
        linestyle="--",
        linewidth=2)

ax.plot(f_carbon, Z_carbon,
        label="|Z| – Carbon resistor",
        linewidth=2)

# Coaxial termination
ax.plot(f_coax, Rs_coax,
        label="Rs – Coaxial termination",
        linestyle="--",
        linewidth=2)

ax.plot(f_coax, Z_coax,
        label="|Z| – Coaxial termination",
        linewidth=2)

# =========================
# Layout
# =========================
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel(r"Resistance / Impedance ($\Omega$)")
# ax.set_title("Comparison of Resistance and Impedance\nCarbon Resistor vs. Coaxial Termination")

ax.grid(True, which="both", linestyle=":", linewidth=0.8)
ax.legend()
plt.xlim(1e6, 30e6)
plt.ylim(48, 52)

fig.tight_layout()

# =========================
# Figure als Pickle speichern
# =========================
fig.savefig("351.pgf")

plt.show()
