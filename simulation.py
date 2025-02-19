from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim

class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        
    def Run(self):
        for i in range(0, 1000):
            time.sleep((1/60))
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)


    def __del__(self):
        p.disconnect()

