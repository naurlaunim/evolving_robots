import pyrosim
import matplotlib.pyplot as plt
import random
from robot import ROBOT

# sim = pyrosim.Simulator()
# sim = pyrosim.Simulator(play_paused = True, eval_time=1000)
for i in range(0, 10):
      sim = pyrosim.Simulator(eval_time=200)

      robot = ROBOT(sim, random.random()*2 - 1)

      sim.start()
      sim.wait_to_finish()


# sensorData = sim.get_sensor_data(sensor_id = T1)
# sensorData = sim.get_sensor_data(sensor_id = P2)
# sensorData = sim.get_sensor_data(sensor_id = P2)
# print(sensorData)

# f = plt.figure()
# panel = f.add_subplot(111)
# # panel.set_ylim(-1, +2)
# plt.plot(sensorData)
# plt.show()