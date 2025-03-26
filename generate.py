import pyrosim.pyrosim as pyrosim
import random

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    z = .5
    size = 1
    pyrosim.Send_Cube(name="Box", pos=[-3 , -3, z], size=[size, size, size])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[0 , 0, .5], size=[1, 1, 1])
    pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name="Link1", pos=[0 , 0, .5], size=[1, 1, 1])
    pyrosim.Send_Joint(name = "Link1_Link2", parent = "Link1", child = "Link2", type = "revolute", position = [0, 0, 1])
    pyrosim.Send_Cube(name="Link2", pos=[0 , 0, .5], size=[1, 1, 1])
    pyrosim.Send_Joint(name = "Link2_Link3", parent = "Link2", child = "Link3", type = "revolute", position = [0, .5, .5])
    pyrosim.Send_Cube(name="Link3", pos=[0 , 0.5, 0], size=[1, 1, 1])
    pyrosim.Send_Joint(name = "Link3_Link4", parent = "Link3", child = "Link4", type = "revolute", position = [0, 1, 0])
    pyrosim.Send_Cube(name="Link4", pos=[0 , .5, 0], size=[1, 1, 1])
    pyrosim.Send_Joint(name = "Link4_Link5", parent = "Link4", child = "Link5", type = "revolute", position = [0, .5, -.5])
    pyrosim.Send_Cube(name="Link5", pos=[0 , 0, -.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name = "Link5_Link6", parent = "Link5", child = "Link6", type = "revolute", position = [0, 0, -1])
    pyrosim.Send_Cube(name="Link6", pos=[0 , 0, -.5], size=[1, 1, 1])
    pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("robot.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-.5,0,1])
    pyrosim.Send_Cube(name = "BackLeg", pos = [-.5, 0, -.5], size=[1, 1, 1])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [.5,0,1])
    pyrosim.Send_Cube(name = "FrontLeg", pos = [.5, 0, -.5], size=[1, 1, 1])
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
    for sensor in range(3):
        for motor in range(3, 5):
            pyrosim.Send_Synapse( sourceNeuronName = sensor , targetNeuronName = motor , weight = random.uniform(-1, 1) )
    pyrosim.End()

Generate_Body()
Generate_Brain()
Create_World()
Create_Robot()

