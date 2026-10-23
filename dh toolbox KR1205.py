import sympy as sp
from sympy.matrices import rot_axis3
# Para el ejemplo donde generamos la matriz DH
from spatialmath import *
from spatialmath.base import *
# Para poder Graficar
import matplotlib.pyplot as plt
import numpy as np
#Para usar el DH
import roboticstoolbox as rtb

# ---------------------------------------------------------------
# KR1205 (7 ejes) - DH estándar
# T_i = Rz(theta_i) * Tz(d_i) * Tx(a_i) * Rx(alpha_i)
# Unidades: metros y radianes (la tabla está en mm y grados)
#
#  i | theta_i | d_i (mm)  | a_i | alpha_i (deg)
#  1 | 90      | 309       | 0   | -90
#  2 | 0       | 198       | 0   |  90
#  3 | 0       | 622       | 0   |  90
#  4 | 0       | 175       | 0   | -90
#  5 | 0       | 577 + 67  | 0   |  90
#  6 | 0       | 103       | 0   |  90
#  7 | 0       | D7        | 0   |   0     <- articulación 7 / herramienta
#
# theta1 = 90 de la tabla se mete como offset de la articulación 1.
# ---------------------------------------------------------------

# D7: longitud de la herramienta en metros (0 = sin herramienta).
# *** Cuando se tenga la medida de la herramienta, cambiarla aquí ***
D7 = 0.0

# Límites de articulación (grados).
# La hoja técnica del KR1205 sólo indica +/- 360 grados de rango general.
# La articulación 2 NO puede dar la vuelta completa (chocaría con el piso),
# por eso se limita a +/- 90 grados. *** Ajustar JOINT2_LIM si se conoce el valor real ***
d2r = np.deg2rad
LIM   = [-2*np.pi, 2*np.pi]          # +/- 360 (hoja técnica)
LIM_2 = [d2r(-90), d2r(90)]          # articulación 2 (piso)

#Ahora usando el DH con Toolbox *************
robot = rtb.DHRobot(
[
    rtb.RevoluteDH(d=0.309,          a=0, alpha=-np.pi/2, offset=np.pi/2, qlim=LIM),
    rtb.RevoluteDH(d=0.198,          a=0, alpha= np.pi/2, qlim=LIM_2),
    rtb.RevoluteDH(d=0.622,          a=0, alpha= np.pi/2, qlim=LIM),
    rtb.RevoluteDH(d=0.175,          a=0, alpha=-np.pi/2, qlim=LIM),
    rtb.RevoluteDH(d=0.577 + 0.067,  a=0, alpha= np.pi/2, qlim=LIM),
    rtb.RevoluteDH(d=0.103,          a=0, alpha= np.pi/2, qlim=LIM),
    rtb.RevoluteDH(d=D7,             a=0, alpha=0,        qlim=LIM),
], name="KR1205", base=SE3(0,0,0))
print(robot)

#Para modificar los angulos comodamente (el offset de 90 grados de theta1 ya está dentro del robot)
joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0)
joint3 = np.deg2rad(0)
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0)
joint6 = np.deg2rad(0)
joint7 = np.deg2rad(0)

q_actual = [joint1, joint2, joint3, joint4, joint5, joint6, joint7]

T07DH = robot.fkine(q_actual)
print(T07DH)
print("Posición (x, y, z) [m]:", np.round(T07DH.t, 6))

T07DH_all = robot.fkine_all(q_actual)
# print(T07DH_all[1]) #T01
# print(T07DH_all[2]) #T02
# print(T07DH_all[3]) #T03
# print(T07DH_all[4]) #T04
# print(T07DH_all[5]) #T05
# print(T07DH_all[6]) #T06
# print(T07DH_all[7]) #T07

# Definir variables articulares (cada fila es una postura, en rad)
q=np.array([[0, 0, 0, 0, 0, 0, 0],
            [d2r(30), 0, 0, 0, 0, 0, 0],
            [d2r(30), d2r(30), 0, 0, 0, 0, 0],
            [d2r(30), d2r(30), d2r(30), 0, 0, 0, 0],
            [d2r(30), d2r(30), d2r(30), d2r(30), 0, 0, 0],
            [d2r(30), d2r(30), d2r(30), d2r(30), d2r(30), 0, 0],
            [d2r(30), d2r(30), d2r(30), d2r(30), d2r(30), d2r(30), 0],
            [d2r(30), d2r(30), d2r(30), d2r(30), d2r(30), d2r(30), d2r(30)],
            [d2r(30), d2r(30), d2r(30), d2r(30), d2r(30), d2r(30), 0],
            [d2r(30), d2r(30), d2r(30), d2r(30), d2r(30), 0, 0],
            [d2r(30), d2r(30), d2r(30), d2r(30), 0, 0, 0],
            [d2r(30), d2r(30), d2r(30), 0, 0, 0, 0],
            [d2r(30), d2r(30), 0, 0, 0, 0, 0],
            [d2r(30), 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]])

# Graficar con posiciones q, una cada 3 segundos
robot.plot(q=q, backend='pyplot', dt=3, limits=[-1.5,1.5,-1.5,1.5,0,2], shadow=True, jointaxes=True)

# Graficar y salvar video
# robot.plot(q=q, backend='pyplot', dt=3, limits=[-1.5,1.5,-1.5,1.5,0,2], shadow=True, loop=False, jointaxes=True, movie="robot.gif")

# Graficar con controlador
q1=np.array([[0, 0, 0, 0, 0, 0, 0]])
robot.teach(q1)