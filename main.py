import pygame
from src import questions

from pygame.locals import (
    KEYDOWN,
    MOUSEBUTTONDOWN,
    K_ESCAPE,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            running = False