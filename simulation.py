import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random 

backLegAmplitude = np.pi/3
backLegFrequency = 9
backLegPhaseOffset = 0

frontLegAmplitude = np.pi/6
frontLegFrequency = 9
frontLegPhaseOffset = np.pi/6

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("robot.urdf")
#p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
frontLegTargetAngles = frontLegAmplitude *np.sin(frontLegFrequency * np.linspace(0, 2*np.pi, 1000) + frontLegPhaseOffset)
backLegTargetAngles = backLegAmplitude *np.sin(backLegFrequency * np.linspace(0, 2*np.pi, 1000) + backLegPhaseOffset)
print(frontLegTargetAngles)
#np.save(file = "data/backLegtargetAngles", arr = backLegTargetAngles)
np.save(file = "data/frontLegtargetAngles", arr = frontLegTargetAngles)

#exit()
for i in range(0, 1000):
    time.sleep((1/60))
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b"Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = backLegTargetAngles[i],
    maxForce = 25)
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b"Torso_FrontLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = frontLegTargetAngles[i],
    maxForce = 25)

#np.save(file = "data/backLegSensorValues.npy", arr = backLegSensorValues)
#np.save(file = "data/frontLegSensorValues.npy", arr = frontLegSensorValues)
p.disconnect()