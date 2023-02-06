import copy
import pickle
from individual import INDIVIDUAL

parent = INDIVIDUAL()
parent.Evaluate(False)
print(parent.fitness)
for i in range(0, 50):
    child = copy.deepcopy(parent)
    child.Mutate()
    child.Evaluate(True)
    # print(parent.fitness, child.fitness)
    print('[g:', i, '] [pw:', parent.genome, '] [p:', parent.fitness, '] [c:', child.fitness, ']')
    if (child.fitness > parent.fitness):
        parent = child
        parent.Evaluate(False)
        f = open('robot.p', 'wb')
        pickle.dump(parent, f)
        f.close()

