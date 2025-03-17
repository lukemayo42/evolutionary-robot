import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time

class SOLUTION:
    def __init__(self, myID):
        self.weights = np.random.rand(3, 2) * 2 -1
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
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-.5,0,1])
        pyrosim.Send_Cube(name = "BackLeg", pos = [-.5, 0, -.5], size=[1, 1, 1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [.5,0,1])
        pyrosim.Send_Cube(name = "FrontLeg", pos = [.5, 0, -.5], size=[1, 1, 1])
        pyrosim.End()

    def Generate_Brain(self):
        filename = f"brain{self.myID}.nndf"
        #print(filename)
        pyrosim.Start_NeuralNetwork(filename)
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + 3 , weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()

    def Mutate(self):
        row = random.randint(0,2)
        column = random.randint(0, 1)
        self.weights[row, column] = random.random() * 2 -1

    def Set_ID(self, ID):
        self.myID = ID
