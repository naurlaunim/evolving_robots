import random
import math
import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT

class INDIVIDUAL:
    def __init__(self):
        self.genome = random.random() * 2 - 1
        self.fitness = 0

        # print(self.genome)

    def Evaluate(self, pb):
        sim = pyrosim.Simulator(eval_time=200, play_blind = pb)

        robot = ROBOT(sim, self.genome)

        sim.start()
        sim.wait_to_finish()

        # x = sim.get_sensor_data(sensor_id=robot.P4, svi = 0)
        y = sim.get_sensor_data(sensor_id=robot.P4, svi = 1)
        # z = sim.get_sensor_data(sensor_id=robot.P4, svi = 2)
        # sensorData = y
        # print(sensorData[-1])
        self.fitness = y[-1]

    def Mutate(self):
        self.genome = random.gauss(self.genome, math.fabs(self.genome))