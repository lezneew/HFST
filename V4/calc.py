import numpy as np
import sympy as sp
n = sp.symbols('n', integer=True, positive=True)
pi = sp.pi
for n in range(1, 12):
    expr = -2 * sp.Rational(1, n) * (-1)**n
    print(f"n={n}: {expr}, {expr/n}")
print()
for n in range(1, 12):
    expr = 2 * (1 - (-1)**n) / (pi * n**2)
    print(f"n={n}: {sp.simplify(expr)}, {sp.simplify(expr/n)}")
print()
for n in range(1, 12):
    expr = (1 - (-1) ** n) / (pi * n )
    print(f"n={n}: {sp.simplify(expr)}, {sp.simplify(expr / n)}")