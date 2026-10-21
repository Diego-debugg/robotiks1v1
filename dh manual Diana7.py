import sympy as sp
import numpy as np

# ---------------------------------------------------------------
# Cinemática directa DH estándar - DIANA 7 (7 GDL)
# T_i = Rz(theta_i) * Tz(d_i) * Tx(a_i) * Rx(alpha_i)
# Unidades: metros y radianes (tu tabla está en mm y grados)
# ---------------------------------------------------------------

theta, d, a, alpha = sp.symbols('theta, d, a, alpha')

# Matriz DH genérica
T = sp.Matrix([
    [sp.cos(theta), -sp.sin(theta) * sp.cos(alpha),  sp.sin(theta) * sp.sin(alpha), a * sp.cos(theta)],
    [sp.sin(theta),  sp.cos(theta) * sp.cos(alpha), -sp.cos(theta) * sp.sin(alpha), a * sp.sin(theta)],
    [0,              sp.sin(alpha),                  sp.cos(alpha),                 d],
    [0,              0,                              0,                             1]
])

q = sp.symbols('theta_1:8')  # theta_1 ... theta_7

# ---------------------------------------------------------------
# D7: distancia desde el marco 6 hasta la brida/herramienta (en metros)
# *** COMPLETAR con tu valor. Con 0.0 el marco 7 queda en el origen del marco 6 ***
# ---------------------------------------------------------------
D7 = 0.0

# ---------------------------------------------------------------
# TABLA DH (tus datos)
#  i | theta_i | d_i (mm) | a_i | alpha_i (deg)
#  1 | theta_1 |   285    |  0  |   90
#  2 | theta_2 |    0     |  0  |  -90
#  3 | theta_3 |   458    |  0  |   90
#  4 | theta_4 |    0     |  0  |  -90
#  5 | theta_5 |   455    |  0  |   90
#  6 | theta_6 |    0     |  0  |   90
#  7 | theta_7 |   D7     |  0  |    0     <- fila nueva (articulación 7)
# ---------------------------------------------------------------
R = sp.Rational
dh_table = [
    # (d,          a, alpha)
    (R(285, 1000), 0,  sp.pi/2),
    (0,            0, -sp.pi/2),
    (R(458, 1000), 0,  sp.pi/2),
    (0,            0, -sp.pi/2),
    (R(455, 1000), 0,  sp.pi/2),
    (0,            0,  sp.pi/2),
    (sp.nsimplify(D7), 0, 0),
]

# Matrices individuales T01 ... T67
Ts = []
for i, (di, ai, ali) in enumerate(dh_table):
    Ti = T.subs({d: di, a: ai, alpha: ali, theta: q[i]})
    Ts.append(Ti)
    print(f"\nT{i}{i+1}:")
    sp.pprint(Ti)

# Transformación total base -> efector final (simplificando paso a paso)
T07 = sp.eye(4)
for Ti in Ts:
    T07 = (T07 @ Ti).applyfunc(sp.simplify)

print("\nT07 simbólica:")
sp.pprint(T07)

# Para exportar a LaTeX:
# print(sp.latex(T07))

# ---------------------------------------------------------------
# EVALUACIÓN NUMÉRICA (ángulos en grados)
# ---------------------------------------------------------------
angulos_deg = [0, 0, 0, 0, 0, 0, 0]  # joint1 ... joint7
subs = {q[i]: np.deg2rad(angulos_deg[i]) for i in range(7)}

T07_num = T07.subs(subs).applyfunc(lambda x: sp.nsimplify(sp.N(x, 12), tolerance=1e-9))
print("\nT07 con los ángulos dados:")
sp.pprint(T07_num)

print("\nPosición del efector final (x, y, z) en metros:")
print([float(T07_num[i, 3]) for i in range(3)])