import copy
import random

from individual import INDIVIDUAL


class POPULATION:
    def __init__(self, popSize):
        self.p = {}
        self.popSize = popSize

    def Print(self):
        for i in self.p:
            if i in self.p:
                self.p[i].Print()
        print()

    def Evaluate(self, pb = True):
        for i in self.p:
            # self.p[i].Evaluate(False)
            self.p[i].Start_Evaluation(pb)
        for i in self.p:
            self.p[i].Compute_Fitness()

    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self, other):
        for i in self.p:
            if self.p[i].fitness < other.p[i].fitness:
                self.p[i] = other.p[i]

                # self.p[i] = other.p[i]

    def Initialize(self):
        for i in range(self.popSize):
            self.p[i] = INDIVIDUAL(i)

    def Fill_From(self, other):
        self.Copy_Best_From(other)
        self.Collect_Children_From(other)

        # print('pop')
        # self.Print()

    def Copy_Best_From(self, other):
        max_fit = 0
        max_i = None
        for i in other.p:
            if other.p[i].fitness > max_fit:
                max_fit = other.p[i].fitness
                max_i = i
        unit = copy.deepcopy(other.p[max_i])
        self.p[0] = unit

    def Collect_Children_From(self, other):
        for i in range(1, self.popSize):
            winner = other.Winner_Of_Tournament_Selection()
            self.p[i] = copy.deepcopy(winner)
            self.p[i].Mutate()

    def Winner_Of_Tournament_Selection(other):
        p1 = random.randint(0, other.popSize-1)
        p2 = random.randint(0, other.popSize-1)
        while p1 == p2:
            p2 = random.randint(0, other.popSize-1)
        if other.p[p1].fitness > other.p[p2].fitness:
            return other.p[p1]
        else:
            return other.p[p2]