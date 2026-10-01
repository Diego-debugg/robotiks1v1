#import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

# from sympy import Symbol, Matrix

# theta = Symbol('theta')
thetadeg = 9
thetarad = np.deg2rad(thetadeg)
# R = rot2(thetarad)
# print(R)

t0 = transl2(0, 0)  # traslación de 1 en x

ta = transl2(1, 2) @trot2(30,"deg")  # rotación de 30 grados y traslación de 1 en x
print(ta)

P = np.array([4, 3])  # punto en coordenadas homogéneas
plot_point(P, "ko", text="P")
print(P)

p1 = homtrans(np.linalg.inv(ta), P)
print(p1)

#rotación de 30 grados y traslación de 1 en x
# print(tb)
# thetadeg2 = 60
# thetarad2 = np.deg2rad(thetadeg2)
# R2 = trot2(thetarad)
# print(R2)


trplot2(t0, frame="0", color="k") #dibujamos en plot
trplot2(ta, frame="A", color="b") #dibujamos en plot
# plot2(tb, frame="B", color="g") #dibujamos en plot

# trplot2(R2) #dibujamos en plot

plt.axis('equal')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Transformación 2D')
plt.show() #Mostrar ventana de plot

