import numpy as np
import matplotlib.pyplot as plt
from spatialmath.base import *   # transl2, trot2, trplot2, plot_circle, plot_point

# PARAMETROS DEL BRAZO PLANAR 3R
L1 = 5        # longitud del eslabón 1
L2 = 3.5      # longitud del eslabón 2
L3 = 2        # longitud del eslabón 3
th1 = 90      # ángulo de la articulación 1 (grados)
th2 = 60      # ángulo de la articulación 2 (grados)
th3 = 45     # ángulo de la articulación 3 (grados)


# Marco base 0: en el origen, sin rotación
T0 = transl2(0, 0)
trplot2(T0, frame="0", color="k")

# Marco 1: solo gira th1 sobre el origen
T1 = trot2(th1, "deg")
trplot2(T1, frame="1", color="b")
# Círculo de alcance del eslabón 1: centrado en el origen
plot_circle(L1, (0, 0), 'b--')

# Marco 2: avanza L1 sobre el eje x del marco 1 y luego gira th2
T2 = T1 @ transl2(L1, 0) @ trot2(th2, "deg")
trplot2(T2, frame="2", color="g")
o2 = T2[:2, 2]   # posición (x, y) del origen del marco 2
# Círculo del eslabón 2: centrado en la articulación 2
plot_circle(L2, (o2[0], o2[1]), 'g--')

# Marco 3: avanza L2 sobre el eje x del marco 2 y luego gira th3
T3 = T2 @ transl2(L2, 0) @ trot2(th3, "deg")
trplot2(T3, frame="3", color="m")
o3 = T3[:2, 2]   # posición del origen del marco 3
# Círculo del eslabón 3: centrado en la articulación 3
plot_circle(L3, (o3[0], o3[1]), 'm--')

# Marco del efector final: avanza L3 sobre el eje x del marco 3, sin giro extra
TE = T3 @ transl2(L3, 0)
trplot2(TE, frame="E", color="r")
oE = TE[:2, 2]   # posición del efector final

# Dibujo los eslabones como líneas entre los orígenes de los marcos
plt.plot([0, o2[0], o3[0], oE[0]], [0, o2[1], o3[1], oE[1]], 'k-', linewidth=2)

# Marco el efector con un punto y muestro su posición en consola
plot_point(oE, "ko", text="P")
print("Efector final: x = {:.4f}, y = {:.4f}".format(oE[0], oE[1]))

# Ajustes de la gráfica
plt.axis('equal')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Brazo planar 3R: th = ({th1}, {th2}, {th3})°')
plt.show()