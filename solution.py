import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, myID):
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 -1
        self.myID = myID

    def Evaluate(self, value):
        pass

    def Start_Simulation(self, value):
        self.Generate_Body()
        self.Generate_Brain()
        os.system(f"start /B python simulate.py {value} {self.myID}")

    def Wait_For_Simulation_To_End(self):
        filename = f"fitness{self.myID}.txt"
        while not os.path.exists(filename):
            time.sleep(0.01)
        file = open(filename, "r")
        self.fitness = float(file.readline())
        file.close()
        #print(self.fitness)
        os.system(f"del fitness{self.myID}.txt")


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        z = .5
        size = 1
        pyrosim.Send_Cube(name="Box", pos=[-3 , -3, z], size=[size, size, size])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("robot.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])
        
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name = "BackLeg", pos = [0, .5, 0], size=[0.2, 1, 0.2])
        
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name = "FrontLeg", pos = [0, -.5, 0], size=[0.2, 1, 0.2])
        
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "LeftLeg", pos = [-.5, 0, 0], size=[1, 0.2, 0.2])
    
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "RightLeg", pos = [.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name = "BackLowerLeg", pos = [0, 0, -.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name = "FrontLowerLeg", pos = [0, 0, -.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "RightLowerLeg", pos = [0, 0, -.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "LeftLowerLeg", pos = [0, 0, -.5], size=[0.2, 0.2, 1])
        pyrosim.End()


    def Generate_Brain(self):
        filename = f"brain{self.myID}.nndf"
        pyrosim.Start_NeuralNetwork(filename)
        #pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        #pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        #pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
        #pyrosim.Send_Sensor_Neuron(name = 3, linkName = "LeftLeg")
        #pyrosim.Send_Sensor_Neuron(name = 4, linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "RightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName = "LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 4, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 6, jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 7, jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 8, jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 9, jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 10, jointName = "RightLeg_RightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 11, jointName = "LeftLeg_LeftLowerLeg")
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()

    def Mutate(self):
        row = random.randint(0,c.numSensorNeurons - 1)
        column = random.randint(0, c.numMotorNeurons - 1)
        self.weights[row, column] = random.random() * (c.numSensorNeurons - 1) - (c.numMotorNeurons - 1)

    def Set_ID(self, ID):
        self.myID = ID
