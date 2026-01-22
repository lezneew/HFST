import numpy as np
import matplotlib.pyplot as plt

# Abschlussimpedanz Zt von 0 bis 250 Ohm
Zt = np.linspace(0, 250, 1000)

# Leitungsimpedanzen
Z0_50 = 50
Z0_75 = 75

# Reflexionsfaktor-Funktion
rho_50 = (Zt - Z0_50) / (Zt + Z0_50)
rho_75 = (Zt - Z0_75) / (Zt + Z0_75)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(Zt, rho_50, label=r"$Z_0 = 50\,\Omega$")
plt.plot(Zt, rho_75, label=r"$Z_0 = 75\,\Omega$")

# Achsen und Beschriftungen
plt.xlabel("Abschlussimpedanz $Z_t$ [Ω]")
plt.ylabel("Reflexionsfaktor $\\rho$")
plt.title("Reflexionsfaktor in Abhängigkeit von der Abschlussimpedanz")

# Hilfslinien
plt.axhline(0, linestyle="--", linewidth=0.8)
plt.axhline(1, linestyle=":", linewidth=0.8)
plt.axhline(-1, linestyle=":", linewidth=0.8)

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
