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
# Load data
# =========================
data = pd.read_csv("3.4.2-lc-bandpass.csv")
data2 = pd.read_csv("342_RL_11.csv")


f = data["Frequency(Hz)"].values
TL_dB = data["Transmission Loss(dB)"].values
# If Return Loss column exists, uncomment the next line
RL_dB = data2["Return Loss(dB)"].values

# If you need to calculate Return Loss from S11 magnitude (|S11|), use:
# RL_dB = -20*np.log10(np.abs(data["S11"]))

# =========================
# Find center frequency and extrema
# =========================
# Center frequency at maximum transmission
idx_max_TL = np.argmin(-TL_dB)  # Transmission Loss is negative in dB
f_center = f[idx_max_TL]
TL_max = TL_dB[idx_max_TL]

# Minimum return loss
# idx_min_RL = np.argmin(RL_dB)
# RL_min = RL_dB[idx_min_RL]

# =========================
# Compute -3 dB bandwidth
# TL_linear = 10^(TL/20)
TL_linear = 10**(-TL_dB / 20)  # linear magnitude, as TL_dB is negative

# Half-power points (-3 dB)
TL_max_linear = np.max(TL_linear)
half_power = TL_max_linear / np.sqrt(2)

# Find indices closest to half-power points on left and right
left_idx = np.where(TL_linear[:idx_max_TL] <= half_power)[0]
right_idx = np.where(TL_linear[idx_max_TL:] <= half_power)[0]

if len(left_idx) > 0:
    f_left = f[left_idx[-1]]
else:
    f_left = f[0]

if len(right_idx) > 0:
    f_right = f[idx_max_TL + right_idx[0]]
else:
    f_right = f[-1]

BW_3dB = f_right - f_left

# =========================
# Plot Transmission Loss
# =========================
fig = plt.figure(figsize=(6.3, 3.5))
plt.plot(f/1e6, TL_dB, linewidth=2, label="Transmission Loss (dB)")
plt.plot(f/1e6, RL_dB, linewidth=2, label="Transmission Loss (dB)")
plt.axvline(f_center/1e6, color='r', linestyle='--', label="Center Frequency")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Transmission Loss (dB)")
plt.title("LC Band-Pass Filter Transmission Loss")
plt.grid(True, linestyle=":", linewidth=0.8)
plt.legend()
plt.tight_layout()
plt.show()

# =========================
# Print results
# =========================
print(f"Center frequency: {f_center/1e6:.3f} MHz")
print(f"Maximum transmission (min TL): {TL_max:.2f} dB")
# print(f"Minimum return loss: {RL_min:.2f} dB")  # Uncomment if RL available
print(f"-3 dB bandwidth: {BW_3dB/1e6:.3f} MHz")
print(f"Lower -3 dB frequency: {f_left/1e6:.3f} MHz")
print(f"Upper -3 dB frequency: {f_right/1e6:.3f} MHz")
fig.savefig("3513.pgf")

# =========================
# Find ALL -3 dB crossing points
# =========================
# Find all indices where TL_linear crosses half_power level
TL_3dB_level = TL_max - 3  # -3 dB level
crossings = []
for i in range(len(TL_dB) - 1):
    tl1, tl2 = TL_dB[i], TL_dB[i + 1]

    # Check if TL_3dB_level is between tl1 and tl2
    if (tl1 - TL_3dB_level) * (tl2 - TL_3dB_level) <= 0:
        # Linear interpolation for more accurate frequency
        f1, f2 = f[i], f[i + 1]
        f_cross = f1 + (TL_3dB_level - tl1) * (f2 - f1) / (tl2 - tl1)
        crossings.append(f_cross)
bw = crossings[1]-crossings[0]
print(crossings)
print(bw)