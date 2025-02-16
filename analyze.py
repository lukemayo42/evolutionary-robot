import numpy as np
import matplotlib.pyplot

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
targetAngles = np.load("data/backLegTargetAngles.npy")
frontLeg = np.load("data/frontLegTargetAngles.npy")
#matplotlib.pyplot.plot(backLegSensorValues, linewidth=2)
#matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.plot(targetAngles)
matplotlib.pyplot.plot(frontLeg)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()