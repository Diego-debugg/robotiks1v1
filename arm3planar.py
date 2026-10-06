import numpy as np
import matplotlib.pyplot as plt
from spatialmath.base import *

# ===== PARÁMETROS =====
L1 = 5
L2 = 3.5
L3 = 2
th1 = 30
th2 = 45
th3 = -30
# ======================

# marco base
T0 = transl2(0, 0)
trplot2(T0, frame="0", color="k")

# marco 1
T1 = trot2(th1, "deg")
trplot2(T1, frame="1", color="b")

# marco 2
T2 = T1 @ transl2(L1, 0) @ trot2(th2, "deg")
trplot2(T2, frame="2", color="g")

# marco 3
T3 = T2 @ transl2(L2, 0) @ trot2(th3, "deg")
trplot2(T3, frame="3", color="m")

# marco del efector final
TE = T3 @ transl2(L3, 0)
trplot2(TE, frame="E", color="r")

# eslabones como líneas entre los orígenes
o2 = T2[:2, 2]
o3 = T3[:2, 2]
oE = TE[:2, 2]
plt.plot([0, o2[0], o3[0], oE[0]], [0, o2[1], o3[1], oE[1]], 'k-', linewidth=2)

plt.axis('equal')
plt.grid(True)
plt.show()