import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class WORLD:
    def __init__(self, value):
        if value == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif value == "GUI":
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0, 0, -9.8)
        self.planeId = p.loadURDF("plane.urdf")