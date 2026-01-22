import sympy as sp

# Symbole
x = sp.symbols('x', real=True)
n = sp.symbols('n', integer=True, positive=True)
pi = sp.pi

# Fourier-Koeffizienten allgemein
def a_n(f):
    return (1/pi) * sp.integrate(f * sp.cos(n*x), (x, -pi, pi))

def b_n(f):
    return (1/pi) * sp.integrate(f * sp.sin(n*x), (x, -pi, pi))

# ----------------------------
# Funktionen aus der Literatur
# ----------------------------

# Sägezahn
f_saw = x

# Dreieck
f_tri = pi - sp.Abs(x)

# Rechteck / Treppenfunktion
f_rect = sp.Piecewise(
    (0, x < 0),
    (1, x > 0)
)

# ----------------------------
# Amplitudenverhältnisse
# ----------------------------

def amplitude_ratio(f, max_n=11):
    ratios = {}
    a1 = a_n(f).subs(n, 1)
    b1 = b_n(f).subs(n, 1)
    A1 = 1# sp.sqrt(a1**2 + b1**2)

    for k in range(1, max_n + 1):
        ak = a_n(f).subs(n, k)
        bk = b_n(f).subs(n, k)
        Ak = sp.sqrt(ak**2 + bk**2)
        ratios[k] = sp.simplify(Ak / A1)

    return ratios

# Berechnung
saw_ratios  = amplitude_ratio(f_saw)
tri_ratios  = amplitude_ratio(f_tri)
rect_ratios = amplitude_ratio(f_rect)

# Ausgabe
print("SÄGEZAHN:")
for k, v in saw_ratios.items():
    print(f"n={k}: {v/k}")

print("\nDREIECK:")
for k, v in tri_ratios.items():
    print(f"n={k}: {v/k}")

print("\nRECHTECK:")
for k, v in rect_ratios.items():
    print(f"n={k}: {v/k}")