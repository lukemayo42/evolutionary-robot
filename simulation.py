from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim

class SIMULATION:
    def __init__(self, value):
        self.value = value
        self.world = WORLD(value)
        self.robot = ROBOT()
        
    def Run(self):
        for i in range(0, 1000):
            if self.value == "GUI":
                time.sleep((1/60))
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)


    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

