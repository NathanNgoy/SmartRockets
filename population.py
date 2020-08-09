from rocket import Rocket
import random

WIDTH = 800
HEIGHT = 700
STARTX = 400
STARTY = HEIGHT - 40

class Population:
    def __init__(self, size = 100):
        self.rockets = []
        self.popsize = size
        self.matingPool = []

        for i in range(self.popsize):
            self.rockets.append(Rocket(STARTX, STARTY))

    def run(self, obstacle):
        for i in range(self.popsize):
            self.rockets[i].update(obstacle)

    def display(self):
        for i in range(self.popsize):
            self.rockets[i].show()

    def evaluate(self):
        maxFit = 0

        for i in range(self.popsize):
            self.rockets[i].calcFitness()
            if (self.rockets[i].fitness > maxFit):
                maxFit = self.rockets[i].fitness
        
        # normalizes fitness
        for i in range(self.popsize):
            self.rockets[i].fitness /= maxFit
        
        self.matingPool = []
        for i in range(self.popsize):
            n = self.rockets[i].fitness * 100
            for j in range(int(n)):
                self.matingPool.append(self.rockets[i])

    def selection(self):
        newRockets = []
        for i in range(self.popsize):
            partner1 = random.choice(self.matingPool).DNA
            partner2 = random.choice(self.matingPool).DNA
            child = partner1.crossover(partner2)
            child.mutation()

            # make a new rocket with new DNA that controls the rocket
            newRockets.append(Rocket(STARTX, STARTY, child))
        self.rockets = newRockets