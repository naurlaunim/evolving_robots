
from individual import INDIVIDUAL

# sim = pyrosim.Simulator()
# sim = pyrosim.Simulator(play_paused = True, eval_time=1000)
for i in range(0, 10):

    individual = INDIVIDUAL()
    individual.Evaluate()
    print(individual.fitness)

# f = plt.figure()
# panel = f.add_subplot(111)
# # panel.set_ylim(-1, +2)
# plt.plot(sensorData)
# plt.show()