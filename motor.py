import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        print(jointName)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.frontLegAmplitude
        self.frequency = c.frontLegFrequency
        self.offset = c.frontLegPhaseOffset
        if self.jointName == b"Torso_BackLeg":
            self.frequency  = self.frequency/2
        print(self.frequency)
        self.motorValues = self.amplitude *np.sin(self.frequency * np.linspace(0, 2*np.pi, 1000) + self.offset)
        #backLegTargetAngles = c.backLegAmplitude *np.sin(c.backLegFrequency * np.linspace(0, 2*np.pi, 1000) + c.backLegPhaseOffset)

    def Set_Value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 25)
        
    def Save_Values(self):
        np.save(file = "data/motorValues.npy", arr = self.motorValues)

            