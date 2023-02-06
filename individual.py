import random
import math
import pyrosim
import numpy, numpy.matlib
import matplotlib.pyplot as plt
from robot import ROBOT

class INDIVIDUAL:
    def __init__(self, i):
        self.genome = numpy.matlib.rand(4, 8) *2 - 1
        self.fitness = 0
        self.ID = i

        # print(self.genome)

    def Evaluate(self, pb):
        self.Start_Evaluation(pb)
        self.Compute_Fitness()

    def Start_Evaluation(self, pb):
        self.sim = pyrosim.Simulator(eval_time=200, play_paused = True, play_blind = pb)

        self.robot = ROBOT(self.sim, self.genome)

        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()

        y = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi = 1)

        self.fitness = y[-1]
        del self.sim

    def Mutate(self):
        geneToMutate = random.randint(0, 3), random.randint(0, 7)
        self.genome[geneToMutate] = random.gauss(self.genome[geneToMutate], math.fabs(self.genome[geneToMutate]))

    def Print(self):
        # print(self.genome)
        print('[', self.ID, ': ', self.fitness, ']', end = ', ')


