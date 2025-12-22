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

files = ["6db.s2p", "10db.s2p", "20db.s2p"]
labels = ["6 dB Attenuator", "10 dB Attenuator", "20 dB Attenuator"]

data_dict = {}

for f, label in zip(files, labels):
    # Read CSV, skip comment lines, assign column names
    df = pd.read_csv(f, comment='!', delim_whitespace=True, header=None,
                     names=["Freq", "S11_dB", "S11_Ang", "S21_dB", "S21_Ang",
                            "S12_dB", "S12_Ang", "S22_dB", "S22_Ang"])

    # Convert relevant columns to numeric
    df["Freq"] = pd.to_numeric(df["Freq"], errors='coerce')
    df["S21_dB"] = pd.to_numeric(df["S21_dB"], errors='coerce')

    # Drop rows where conversion failed
    df = df.dropna(subset=["Freq", "S21_dB"])

    # Sort by frequency to ensure proper plotting
    df = df.sort_values("Freq")

    freq = df["Freq"].values
    S21_dB = df["S21_dB"].values
    S21_lin = 10 ** (S21_dB / 20)  # convert to linear magnitude

    data_dict[label] = {"freq": freq, "S21_dB": S21_dB, "S21_lin": S21_lin}

# =========================
# Create figure with two subplots side by side
# =========================
fig, axes = plt.subplots(1, 2, figsize=(6.3, 3.5))

# First plot: TL in dB
ax1 = axes[0]
for label in labels:
    ax1.plot(data_dict[label]["freq"] / 1e9, data_dict[label]["S21_dB"],
             linewidth=2, label=label)
ax1.set_xlabel("Frequency (GHz)")
ax1.set_ylabel("Transmission Loss |S21| (dB)")
ax1.set_title("Transmission Loss (log scale)")
ax1.grid(True, linestyle=":", linewidth=0.8)
ax1.legend()

# Second plot: TL in linear scale
ax2 = axes[1]
for label in labels:
    ax2.plot(data_dict[label]["freq"] / 1e9, data_dict[label]["S21_lin"],
             linewidth=2, )
ax2.set_xlabel("Frequency (GHz)")
ax2.set_ylabel("Transmission Loss |S21| (linear)")
ax2.set_title("Transmission Loss (linear scale)")
ax2.grid(True, linestyle=":", linewidth=0.8)
ax2.legend()

# Adjust layout and save
plt.tight_layout()
fig.savefig("attenuators_comparison.pgf")

# If you specifically want to save as "359.pgf"
fig.savefig("3510.pgf")

plt.show()