import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import time
import constants as c
import numpy as np
import math

class ROBOT:
    def __init__(self, solutionID):
        self.motors = {}
        self.solutionID = solutionID
        time.sleep(0.02)
        self.robotId = p.loadURDF(f"robot{solutionID}.urdf")
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        os.system(f"del brain{solutionID}.nndf")
        os.system(f"del robot{solutionID}.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
          self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
            
                self.motors.get(jointName).Set_Value(self.robotId, desiredAngle)
                jointName = jointName.decode("utf-8")
                #print(f"{neuronName} {jointName} {desiredAngle}")
        #for i in self.motors:
        #    self.motors[i].Set_Value(self.robotId, t)  
    


    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        torso_penalty = 0
        for i in self.sensors["Torso"].values:
            if i == 1:
                torso_penalty = 5
        
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        orientation = basePositionAndOrientation[1]
        xPosition = basePosition[0]
        orientationEuler = p.getEulerFromQuaternion(orientation)
        roll = orientationEuler[0]
        pitch = orientationEuler[1]


        roll_penalty = 0
        # punish high angulation
        # use exp scale to punish high angles
        alpha = 2
        #roll_penalty = math.exp(alpha * abs(roll))
        pitch_penalty = 0
        #pitch_penalty = math.exp(alpha * abs(pitch))


        # punish lower legs dragging on the ground
        # get all the states of the lower leg
        lower_leg_penalty = 0
        for i in range(4, 8):
            lower_leg_info =  p.getLinkState(self.robotId, i)
            lower_leg_orientation = p.getEulerFromQuaternion(lower_leg_info[1])
            print(lower_leg_orientation)
            if (abs(lower_leg_orientation[0]) > 1.55 and abs(lower_leg_orientation[0]) < 1.55) or abs(lower_leg_orientation[1]) > 1.55 and abs(lower_leg_orientation[1]) < 1.56:
                lower_leg_penalty = 10
        #minimize this function, the xPosition of the robot, add 100 if the torso sensor ever goes off, meaning that it touches the ground at any point
        # because if this is the case the robot has likely flipped over.
        fitness = xPosition + torso_penalty + roll_penalty + pitch_penalty + lower_leg_penalty

        
        #print(xCoordinateOfLinkZero)
        f = open(f"tmp{self.solutionID}.txt", "w")
        f.write(str(fitness))
        f.close()
        os.system(f"rename tmp{self.solutionID}.txt fitness{self.solutionID}.txt")
        #exit()

    def print_orientation(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        orientation = basePositionAndOrientation[1]
        orientationEuler = p.getEulerFromQuaternion(orientation)
        print(orientationEuler)