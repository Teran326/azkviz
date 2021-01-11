#para = parametry
import pygame
running = True
obrazovka_x = 1000
obrazovka_y = 1000
obrazovka = pygame.display.set_mode((obrazovka_x, obrazovka_y))
#velikost určuje délku jedné hrany šestiúhelníka (r)
velikost = 50
#vrcholy pyramidy šestiúhelníků
vrchol_x = obrazovka_x/2
vrchol_y = 100
blue = (0,255,0)
#o kolikatou radu se jedná
rada = 0
#mezera mezi šestiúhelníky
mezera = 10
#ocislovani
ocislovani = 1


from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    RLEACCEL,
    MOUSEBUTTONDOWN
)