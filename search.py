import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER


phca = PARALLEL_HILL_CLIMBER("b")

phca.Evolve()
phca.Show_Best()
phca.save_data()

"""
phcb = PARALLEL_HILL_CLIMBER("b")
phcb.Evolve()
phcb.Show_Best()
"""

'''
for i in range(5):
    os.system("python generate.py")
    os.system("python simulate.py")'
    '''