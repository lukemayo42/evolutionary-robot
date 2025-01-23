import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
z = .5
size = 1
for x in range(0, 5):
    for y in range(0, 5):
        size = 1
        z = .5
        for i in range(0, 10):
            pyrosim.Send_Cube(name="Box", pos=[x , y, z], size=[size, size, size])
            size = size*.9
            z+=1

pyrosim.End()