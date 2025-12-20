import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================
# Load IF filter data
# =========================
data = pd.read_csv("3.4.3-if-bandpass.csv")  # replace with your file

f = data["Frequency(Hz)"].values
TL_dB = data["Transmission Loss(dB)"].values  # transmission loss

# Center frequency
f_center = 10.7e6  # 10.7 MHz

# =========================
# Find maximum transmission near center frequency
# =========================
# Consider a small window around f_center to find peak
window = (f > f_center - 0.5e6) & (f < f_center + 0.5e6)
idx_peak = np.argmax(-TL_dB[window])  # TL_dB is negative
idx_peak_global = np.arange(len(f))[window][idx_peak]

TL_max = TL_dB[idx_peak_global]

# =========================
# 6 dB points (frequencies where TL drops by 6 dB from peak)
TL_6dB = TL_max - 6  # since TL is negative, subtracting 6 dB

# Find left 6 dB point
left_idx = np.where(TL_dB[:idx_peak_global] >= TL_6dB)[0]
if len(left_idx) > 0:
    f_left = f[left_idx[-1]]
else:
    f_left = f[0]

# Find right 6 dB point
right_idx = np.where(TL_dB[idx_peak_global:] >= TL_6dB)[0]
if len(right_idx) > 0:
    f_right = f[idx_peak_global + right_idx[0]]
else:
    f_right = f[-1]

BW_6dB = f_right - f_left

# =========================
# Plot Transmission Loss
# =========================
plt.figure(figsize=(8,5))
plt.plot(f/1e6, TL_dB, linewidth=2, label="Transmission Loss")
plt.axvline(f_center/1e6, color='r', linestyle='--', label="Center Frequency")
plt.axvline(f_left/1e6, color='g', linestyle='--', label="6 dB Points")
plt.axvline(f_right/1e6, color='g', linestyle='--')
plt.xlabel("Frequency (MHz)")
plt.ylabel("Transmission Loss (dB)")
plt.title("IF Filter Transmission Loss with 6 dB Bandwidth")
plt.grid(True, linestyle=":", linewidth=0.8)
plt.legend()
plt.tight_layout()
plt.show()

# =========================
# Print results
# =========================
print(f"Center frequency: {f_center/1e6:.3f} MHz")
print(f"Maximum transmission: {TL_max:.2f} dB")
print(f"6 dB bandwidth: {BW_6dB/1e6:.3f} MHz")
print(f"Lower 6 dB frequency: {f_left/1e6:.3f} MHz")
print(f"Upper 6 dB frequency: {f_right/1e6:.3f} MHz")
