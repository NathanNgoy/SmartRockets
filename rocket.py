import pygame
import numpy as np
import math
from dna import DNA
from obstacle import Obstacle

targetX = 400
targetY = 50
WIDTH = 800
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Rocket:
    def __init__(self, x, y, dna = None):
        # [x-cord, y-cord]
        self.pos = [x, y]
        self.vel = [0, 0]
        self.acc = [0, 0]
        self.completed = False
        self.crashed = False
        self.playerImg = pygame.image.load("rocket.png")
        if dna:
            self.DNA = dna
        else:
            self.DNA = DNA()
        self.count = 0
        self.fitness = 0

    def applyForce(self, force):
        self.acc = np.add(self.acc, force)
    
    def update(self, obstacle):
        # check if target is reached
        d = math.sqrt(math.pow(targetX - self.pos[0], 2) + math.pow(targetY - self.pos[1], 2))
        if (d < 10):
            self.completed = True
            self.pos = [targetX, targetY]

        # add genes into acceleration
        self.applyForce(self.DNA.genes[self.count])
        self.count += 1

        if self.pos[0] > WIDTH or self.pos[0] < 0 or self.pos[1] > HEIGHT or self.pos[1] < 0:
            self.crashed = True

        for i in range(obstacle.count):
            d_obs = math.sqrt(math.pow(obstacle.ob_x[i] + 20 - self.pos[0], 2) + math.pow(obstacle.ob_y[i] + 20 - self.pos[1], 2))
            if d_obs < 20:
                self.crashed = True

        # if target is reached -> stop moving, if target hit wall -> stop moving :: otherwise continue
        if not self.completed and not self.crashed:
            # add acceleration to velocity :: add velocity to position
            self.vel = np.add(self.vel, self.acc)
            self.pos = np.add(self.vel, self.pos)
            self.acc = [0, 0]

    def show(self):
        screen.blit(self.playerImg, (self.pos[0], self.pos[1]))
    
    def calcFitness(self):
        distance = math.sqrt(math.pow(targetX - self.pos[0], 2) + math.pow(targetY - self.pos[1], 2))
        if distance == 0:
            distance = 1
        self.fitness = 1/distance

        if self.completed:
            self.fitness *= 10
        
        if self.crashed:
            self.fitness /= 10