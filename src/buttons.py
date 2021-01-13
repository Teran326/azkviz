import pygame


class Buttons(pygame.sprite.Sprite):
    def __init__(self):
        super(Buttons, self).__init__()
        self.surf = self.surf
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2),)
        )


from pygame.locals import (
    KEYDOWN,
    RLEACCEL,
    MOUSEBUTTONDOWN,
    K_ESCAPE,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

button = Buttons()

all_sprites = pygame.sprite.Group()
all_sprites.add(button)

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
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
    pygame.display.update()