import pygame
from time_commands import *

pygame.init()

screen = pygame.display.set_mode((900, 710))
clock = pygame.time.Clock()
screen.fill((100, 255, 90))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)