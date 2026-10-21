import numpy as np
from spatialmath import SE3
# Para usar el DH con el toolbox
import roboticstoolbox as rtb

# ---------------------------------------------------------------
# DIANA 7 (7 GDL) con Robotics Toolbox - DH estándar
# T_i = Rz(theta_i) * Tz(d_i) * Tx(a_i) * Rx(alpha_i)
# Unidades: metros y radianes
# ---------------------------------------------------------------

# D7: distancia del marco 6 a la brida/herramienta (m).
# *** Completar cuando se tenga la medida. Con 0.0 el marco 7 queda en el centro de la muñeca ***
D7 = 0.0

# Límites de articulación (hoja técnica del Diana 7), en grados -> radianes
lim = lambda lo, hi: [np.deg2rad(lo), np.deg2rad(hi)]

# ---------------------------------------------------------------
# TABLA DH
#  i | theta_i | d_i (mm) | a_i | alpha_i (deg) | rango (deg)
#  1 | theta_1 |   285    |  0  |   90          | -179 a 179
#  2 | theta_2 |    0     |  0  |  -90          |  -90 a 90
#  3 | theta_3 |   458    |  0  |   90          | -179 a 179
#  4 | theta_4 |    0     |  0  |  -90          |    0 a 175
#  5 | theta_5 |   455    |  0  |   90          | -179 a 179
#  6 | theta_6 |    0     |  0  |   90          | -179 a 179
#  7 | theta_7 |   D7     |  0  |    0          | -179 a 179
# ---------------------------------------------------------------
diana7 = rtb.DHRobot(
    [
        rtb.RevoluteDH(d=0.285, a=0, alpha= np.pi/2, qlim=lim(-179, 179)),
        rtb.RevoluteDH(d=0,     a=0, alpha=-np.pi/2, qlim=lim(-90, 90)),
        rtb.RevoluteDH(d=0.458, a=0, alpha= np.pi/2, qlim=lim(-179, 179)),
        rtb.RevoluteDH(d=0,     a=0, alpha=-np.pi/2, qlim=lim(0, 175)),
        rtb.RevoluteDH(d=0.455, a=0, alpha= np.pi/2, qlim=lim(-179, 179)),
        rtb.RevoluteDH(d=0,     a=0, alpha= np.pi/2, qlim=lim(-179, 179)),
        rtb.RevoluteDH(d=D7,    a=0, alpha=0,        qlim=lim(-179, 179)),
    ],
    name="DIANA7", base=SE3(0, 0, 0))
print(diana7)

# Para modificar los ángulos cómodamente (grados)
joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0)
joint3 = np.deg2rad(0)
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0)
joint6 = np.deg2rad(0)
joint7 = np.deg2rad(0)

q_actual = [joint1, joint2, joint3, joint4, joint5, joint6, joint7]

# Cinemática directa base -> efector final (T07)
T07 = diana7.fkine(q_actual)
print(T07)
print("Posición (x, y, z) [m]:", np.round(T07.t, 6))

# Todas las transformaciones acumuladas (T00 ... T07)
T_all = diana7.fkine_all(q_actual)
# print(T_all[1])  # T01
# print(T_all[2])  # T02 ...

# ---------------------------------------------------------------
# Trayectoria de ejemplo (cada fila es una postura, en rad)
# OJO: la articulación 4 sólo admite de 0 a 175 grados
# ---------------------------------------------------------------
d2r = np.deg2rad
q = np.array([
    [0,       0,       0,       0,       0,       0,       0],
    [d2r(30), 0,       0,       0,       0,       0,       0],
    [d2r(30), d2r(30), 0,       0,       0,       0,       0],
    [d2r(30), d2r(30), d2r(30), 0,       0,       0,       0],
    [d2r(30), d2r(30), d2r(30), d2r(60), 0,       0,       0],
    [d2r(30), d2r(30), d2r(30), d2r(60), d2r(45), 0,       0],
    [d2r(30), d2r(30), d2r(30), d2r(60), d2r(45), d2r(30), 0],
    [d2r(30), d2r(30), d2r(30), d2r(60), d2r(45), d2r(30), d2r(45)],
    [0,       0,       0,       0,       0,       0,       0],
])

# Graficar con posiciones q, una cada 3 segundos
diana7.plot(q=q, backend='pyplot', dt=3, limits=[-1, 1, -1, 1, 0, 1.4],
            shadow=True, jointaxes=True)

# Graficar y salvar video
# diana7.plot(q=q, backend='pyplot', dt=3, limits=[-1, 1, -1, 1, 0, 1.4],
#             shadow=True, loop=False, jointaxes=True, movie="diana7.gif")

# Graficar con controlador (sliders)
q1 = np.array([[0, 0, 0, 0, 0, 0, 0]])
diana7.teach(q1)