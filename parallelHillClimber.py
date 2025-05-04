from solution import SOLUTION
import constants as c
import copy
import os
import pybullet as p
import numpy as np

class PARALLEL_HILL_CLIMBER:
    
    def __init__(self, version):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del robot*.urdf")
        self.version = version
        self.parents = {}
        self.nextAvailableID = 0
        for x in range(c.populationSize):
            self.parents[x] = SOLUTION(self.nextAvailableID, self.version, x)
            self.nextAvailableID+=1
        
        self.data = np.zeros((c.populationSize, c.numberOfGenerations))



    def Evolve(self):
        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)

    def Evolve_For_One_Generation(self, genNum):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        for key in self.parents:
            print(self.parents[key].get_fitness())
            self.data[key, genNum] = self.parents[key].get_fitness()


    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID+=1
  

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()
        

    def Select(self):
        for key in self.parents:
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]


    def Print(self):
        for key in self.parents:
            print(f"\nparent:{self.parents[key].fitness}, child:{self.children[key].fitness}\n")

    def Show_Best(self):
        best_key = 0
        for key in self.parents:
            if self.parents[key].fitness <= self.parents[best_key].fitness:
                best_key = key
        
        self.parents[best_key].Start_Simulation("GUI", "t")

    def Evaluate(self, solutions):
        for key in solutions:
            solutions[key].Start_Simulation("DIRECT", "f")

        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()
            #self.data[key, genNum] = solutions[key].fitness

    def save_data(self, name):
        np.save(name, self.data)