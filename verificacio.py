import numpy as np
import roboticstoolbox as rtb

robot=rtb.models.DH.Puma560()

#Variebles articulres

q=[0, np.deg2rad(30), -np.deg2rad(160), 0, 0, 0]

#Visualizar

#robot.plot(q, block=True, backend='pyplot')
#Si se downgreado a matplotlib 3.8.3
robot.teach(q)