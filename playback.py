from individual import INDIVIDUAL
import pickle

f = open('robot0.p', 'rb')

best = pickle.load(f)

f.close()

best.Evaluate(False)
print(best.fitness)