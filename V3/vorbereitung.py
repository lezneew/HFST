import numpy as np
import matplotlib.pyplot as plt

# Parameter

R = 5.0            # Ohm
L = 2.2e-6         # Henry
Z0 = 50.0          # Ohm
f_start = 1e5      # 100 kHz
f_stop  = 2e8      # 200 MHz
N = 2000           # Anzahl Punkte

# Frequenzachse (logarithmisch)

f = np.logspace(np.log10(f_start), np.log10(f_stop), N)
w = 2 * np.pi * f

# Impedanz des DUT: ZL = R + j*w*L

ZL = R + 1j * w * L

# Reflexionsfaktor: Gamma = (ZL - Z0) / (ZL + Z0)

Gamma = (ZL - Z0) / (ZL + Z0)

# Betrag (dB) und Phase (Grad)

mag_db = np.abs(Gamma)#20 * np.log10(np.abs(Gamma))
phase_deg = np.unwrap(np.angle(Gamma)) * 180 / np.pi

# Plot

plt.figure(figsize=(9,6))

plt.subplot(2,1,1)
plt.semilogx(f, mag_db)
plt.grid(True, which='both', ls=':')
plt.ylabel('|r| (dB)')
plt.title('Eingangsreflexion (R=5 Ω, L=2.2 μH, Z0=50 Ω)')

plt.subplot(2,1,2)
plt.semilogx(f, phase_deg)
plt.grid(True, which='both', ls=':')
plt.ylabel('angle(r) (°)')
plt.xlabel('Frequenz (Hz)')

plt.tight_layout()
plt.show()