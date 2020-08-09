import pygame
import time
from rocket import Rocket
from population import Population
from dna import DNA
from obstacle import Obstacle

# Initialize the pygame
pygame.init()

# Create the screen (width, height)
WIDTH = 800
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
rocket_picture = pygame.image.load("rocket.png")
STARTX = 400
STARTY = HEIGHT - 40

# target
planet = pygame.image.load("universe.png")
targetX = 400
targetY = 50

#DNA
lifespan = 200

# run
RUN = 0
generation = 1
font = pygame.font.Font("freesansbold.ttf", 15)
textX = 10
textY = 10

# question
q_font = pygame.font.Font("freesansbold.ttf", 15)

def population_run(population, obstacle):
    screen.fill((0,0,0))
    population.run(obstacle)
    population.display()
    target()

def show_run(x, y, run, gen):
    score = font.render("Gen: " + str(gen) + " - " + str(run), True, (255, 255, 255))
    screen.blit(score, (x, y))

def target():
    screen.blit(planet, (targetX, targetY))

def obstacle_question(x, y):
    question = q_font.render("Click on screen to place obstacles, press Y when done, press R to reset obstacles", True, (255, 255, 255))
    screen.blit(question, (x, y))

def start_screen_rocket():
    screen.blit(rocket_picture, (STARTX, STARTY))

pop = Population()
obs = Obstacle()

# Setting up obstacles
setting = True
running = True
has_obs = False

while setting:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            setting = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                setting = False
            if event.key == pygame.K_r:
                obs.clear_obstacle()
                has_obs = False
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            obs.make_obstacle(pos[0], pos[1])
            has_obs = True
    
    obstacle_question(textX, textY)
    obs.display()
    target()
    start_screen_rocket()

    pygame.display.update()

# Game Loop
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    population_run(pop, obs)
    show_run(textX, textY, RUN, generation)

    RUN += 1
    if RUN == lifespan:
        pop.evaluate()
        pop.selection()
        RUN = 0
        generation += 1

    if has_obs:
        obs.display()

    pygame.display.update()

    time.sleep(1/60)