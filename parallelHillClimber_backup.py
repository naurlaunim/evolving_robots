# import copy
# import pickle
from population import POPULATION

pop = POPULATION(5)
pop.Evaluate()
pop.Print()
# parent = INDIVIDUAL()
# parent.Evaluate(True)
# print(parent.fitness)
# for i in range(0, 1000):
#     child = copy.deepcopy(parent)
#     child.Mutate()
#     child.Evaluate(True)
#     # print(parent.fitness, child.fitness)
#     print('[g:', i, '] [pw:', parent.genome, '] [p:', parent.fitness, '] [c:', child.fitness, ']')
#     if (child.fitness > parent.fitness):
#         parent = child
#         parent.Evaluate(True)
#         f = open('robot0.p', 'wb')
#         pickle.dump(parent, f)
#         f.close()
#
