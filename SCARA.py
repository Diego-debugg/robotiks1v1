#import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

t0 = transl2(0, 0)  # traslación de 1 en x
trplot2(t0, frame="0", color="k") #dibujamos en plot
L1= 4
L2= 3
J1= 45
J2= 60

Ta= trot2(J1, "deg")
trplot2(Ta, frame="A", color="b") #dibujamos en plot
plot_circle(L1, (0,0), 'b--')

Tba= Ta@transl2(L1,0) @trot2(J2, "deg")
trplot2(Tba, frame="BA", color="g") #dibujamos en plot
origin_Tba=Tba[:2,2]
plot_circle(L2, (origin_Tba[0], origin_Tba[1]), 'g--')

Tcba=Tba@transl2(L2,0)
trplot2(Tcba, frame="CBA", color="r") #dibujamos en plot
print(Tcba)

origin_Tcba=Tcba[:2,2]
P=np.array([origin_Tcba[0], origin_Tcba[1]])
plot_point(P, "ko", text="p")
print("Coordenadas en TO: {:.4f}, {:.4f}".format(P[0], P[1]))

P_TA = homtrans(np.linalg.inv(Ta), P)
print(f"Coordenadas en TA: {P_TA[0, 0]:.4f}, {P_TA[1, 0]:.4f}")

P_TBA = homtrans(np.linalg.inv(Tba), P)
print(f"Coordenadas en TBA: {P_TBA[0, 0]:.4f}, {P_TBA[1, 0]:.4f}")

plt.axis('equal')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Transformación 2D')
plt.show() #Mostrar ventana de plot