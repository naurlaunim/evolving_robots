import copy
# import pickle
from population import POPULATION

popSize = 10
parents = POPULATION(popSize)
parents.Initialize()
parents.Evaluate(True)
# exit()
print(0, end = '  ')
parents.Print()

for g in range(1, 1000):
    children = POPULATION(popSize)
    children.Fill_From(parents)
    children.Collect_Children_From(parents)
    children.Evaluate()
    # print(g,  end = '  ')
    # children.Print()
    # exit()
    parents.ReplaceWith(children)
    parents.ReplaceWith(children)
    print(g, end = '  ')
    parents.Print()
parents.p[0].Evaluate(False)

