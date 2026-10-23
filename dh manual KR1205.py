import sympy as sp
from sympy.matrices import rot_axis3
# To be able to plot
import matplotlib.pyplot as plt
import numpy as np
# To generate the DH matrix
from spatialmath import *
from spatialmath.base import *

# Define the symbols
theta, d, a, alpha = sp.symbols('theta, d, a, alpha')

# RzTzTxRx matrix
TDH= trotz(theta) @ transl(0,0, d) @ transl(a,0, 0) @ trotx(alpha) # type: ignore
sp.pprint(TDH)
print(type(TDH))

#Declaring it explicitly
T = sp.Matrix([
    [sp.cos(theta), -sp.sin(theta) * sp.cos(alpha), sp.sin(theta) * sp.sin(alpha), a * sp.cos(theta)],
    [sp.sin(theta), sp.cos(theta)* sp.cos(alpha), -sp.cos(theta) * sp.sin(alpha), a * sp.sin(theta)],
    [0, sp.sin(alpha), sp.cos(alpha), d],
    [0, 0, 0, 1]
])
sp.pprint(T)
print(type(T))

theta_1, theta_2,theta_3, theta_4,theta_5, theta_6  = sp.symbols('theta_1, theta_2,theta_3, theta_4,theta_5, theta_6')
#From the DH table (mm -> m, grados -> rad)
#  i | theta_i | d_i (mm)  | a_i | alpha_i
#  1 | 90      | 309       | 0   | -90
#  2 | 0       | 198       | 0   |  90
#  3 | 0       | 622       | 0   |  90
#  4 | 0       | 175       | 0   | -90
#  5 | 0       | 577 + 67  | 0   |  90
#  6 | 0       | 103       | 0   |  90
T01 = T.subs({d: 0.309, a: 0, alpha: -sp.pi/2}) #theta1+sp.pi/2
T01 = T01.subs({theta: theta_1})
sp.pprint(T01)

T12 = T.subs({d: 0.198, a: 0, alpha: sp.pi/2})
T12 = T12.subs({theta: theta_2})
sp.pprint(T12)

T23 = T.subs({d: 0.622, a: 0, alpha: sp.pi/2})
T23 = T23.subs({theta: theta_3})
sp.pprint(T23)

T34 = T.subs({d: 0.175, a: 0, alpha: -sp.pi/2})
T34 = T34.subs({theta: theta_4})
sp.pprint(T34)

T45 = T.subs({d: 0.577 + 0.067, a: 0, alpha: sp.pi/2})
T45 = T45.subs({theta: theta_5})
sp.pprint(T45)

T56 = T.subs({d: 0.103, a: 0, alpha: sp.pi/2})
T56 = T56.subs({theta: theta_6})
sp.pprint(T56)

T06 = T01 @ T12 @ T23 @ T34 @ T45 @ T56
T06_s= T06.applyfunc(sp.simplify)
sp.pprint(T06_s)

#To export to LaTeX
# latex_str = sp.latex(T06_s)
# print(latex_str)

#EXAMPLE AND QUICK VALIDATION
#To change the angles conveniently
joint1 = np.deg2rad(0) + sp.pi/2 #Offset (theta1 = 90 en la tabla)
joint2 = np.deg2rad(0)
joint3 = np.deg2rad(0)
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0)
joint6 = np.deg2rad(0)

T06_solved = T06_s.subs({theta_1: joint1, theta_2: joint2,theta_3: joint3,theta_4: joint4,theta_5: joint5,theta_6: joint6})
sp.pprint(T06_solved)

print("\nPosición del efector final (x, y, z) en metros:")
print([float(T06_solved[i, 3]) for i in range(3)])