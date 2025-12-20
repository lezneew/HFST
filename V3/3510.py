import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

files = ["6db.s2p", "10db.s2p", "20db.s2p"]
labels = ["6 dB Attenuator", "10 dB Attenuator", "20 dB Attenuator"]

data_dict = {}

for f, label in zip(files, labels):
    # Read CSV, skip comment lines, assign column names
    df = pd.read_csv(f, comment='!', delim_whitespace=True, header=None,
                     names=["Freq", "S11_dB", "S11_Ang", "S21_dB", "S21_Ang",
                            "S12_dB", "S12_Ang", "S22_dB", "S22_Ang"])

    # Convert S21_dB and Freq to numeric
    df["Freq"] = pd.to_numeric(df["Freq"], errors='coerce')
    df["S21_dB"] = pd.to_numeric(df["S21_dB"], errors='coerce')

    # Drop rows where conversion failed
    df = df.dropna(subset=["Freq", "S21_dB"])

    freq = df["Freq"].values
    S21_dB = df["S21_dB"].values
    S21_lin = 10 ** (S21_dB / 20)  # convert to linear magnitude

    data_dict[label] = {"freq": freq, "S21_dB": S21_dB, "S21_lin": S21_lin}

# =========================
# Plot TL in dB
# =========================
plt.figure(figsize=(8, 5))
for label in labels:
    plt.plot(data_dict[label]["freq"] / 1e9, data_dict[label]["S21_dB"], linewidth=2, label=label)
plt.xlabel("Frequency (GHz)")
plt.ylabel("Transmission Loss |S21| (dB)")
plt.title("Transmission Loss (log scale) for 3 Attenuators")
plt.grid(True, linestyle=":", linewidth=0.8)
plt.legend()
plt.tight_layout()
plt.show()

# =========================
# Plot TL in linear scale
# =========================
plt.figure(figsize=(8, 5))
for label in labels:
    plt.plot(data_dict[label]["freq"] / 1e9, data_dict[label]["S21_lin"], linewidth=2, label=label)
plt.xlabel("Frequency (GHz)")
plt.ylabel("Transmission Loss |S21| (linear)")
plt.title("Transmission Loss (linear scale) for 3 Attenuators")
plt.grid(True, linestyle=":", linewidth=0.8)
plt.legend()
plt.tight_layout()
plt.show()
