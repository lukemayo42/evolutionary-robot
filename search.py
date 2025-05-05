import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
#import plotFitnessValues as plt

#phca = PARALLEL_HILL_CLIMBER("a")

#phca.Evolve()
#phca.Show_Best()
#phca.save_data("dataA.npy")


phcb = PARALLEL_HILL_CLIMBER("b")
phcb.Evolve()
phcb.Show_Best()
#phcb.save_data("dataB.npy")

#plt.plot()