import copy
# import pickle
from population import POPULATION

parents = POPULATION(10)
parents.Evaluate()
# exit()
parents.Print()

for g in range(1000):
    children = copy.deepcopy(parents)
    children.Mutate()
    children.Evaluate()
    # children.Print()

    parents.ReplaceWith(children)
    print(g, end = '  ')
    parents.Print()
parents.Evaluate(False)
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
