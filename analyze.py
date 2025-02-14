import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
matplotlib.pyplot.plot(backLegSensorValues, linewidth=2)
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()