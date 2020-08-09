import pygame
WIDTH = 800
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Obstacle:
    def __init__(self):
        self.ob_img = []
        self.ob_x = []
        self.ob_y = []
        self.count = 0

    def display(self):
        for i in range(self.count):
            screen.blit(self.ob_img[i], (self.ob_x[i], self.ob_y[i]))

    def return_count(self):
        return self.count
    
    def make_obstacle(self, x, y):
        obj = pygame.image.load("meteor.png")
        self.ob_img.append(obj)
        self.ob_x.append(x)
        self.ob_y.append(y)
        self.count += 1

    def clear_obstacle(self):
        self.ob_list = []
        self.ob_x = []
        self.ob_y = []
        self.count = 0




