#para = parametry
import pygame
import math

#POKUD ZBYDE CAS MENU S TĚMITO HODNOTAMI
#velikost určuje délku jedné hrany šestiúhelníka (r)
velikost = 25
#pocet rad šestiúhelníků ve hře
zadano = 10


running = True
obrazovka_x = 1000
obrazovka_y = 1000
obrazovka = pygame.display.set_mode((obrazovka_x, obrazovka_y))
#vrcholy pyramidy šestiúhelníků
vrchol_x = obrazovka_x/2
vrchol_y = 2500/(velikost*2)
red = (255,0,0,255)
redPlayer = (255,0,0,254)
#mezera mezi šestiúhelníky
mezera = velikost/3
#o kolikatou radu se jedná
rada = 0
#ocislovani
ocislovani = 0
#cisla pro barvu
bc = 0
#odsazení šestiúhelnkíků
odsazeni_x = 2*velikost
#odsazeni_y = math.ceil(velikost/10)
odsazeni_y = 2*velikost - mezera



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