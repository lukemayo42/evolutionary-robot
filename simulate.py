from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
p = sys.argv[3]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()
if p == "t":
    simulation.robot.print_orientation()

