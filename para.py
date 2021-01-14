#para = parametry
import pygame
import math

#POKUD ZBYDE CAS MENU S TĚMITO HODNOTAMI
#velikost určuje délku jedné hrany šestiúhelníka (r)
velikost = 25
#pocet rad šestiúhelníků ve hře
zadano = 15
#True modrý
#False orandžový
zacinajici_hrac = True

premena2 = ""
premena = False

running = True
#zacatek je k tomu aby se barvy nehodily hned pokud není otázka
zacatek = True
obrazovka_x = 1000
obrazovka_y = 1000
obrazovka = pygame.display.set_mode((obrazovka_x, obrazovka_y))
#vrcholy pyramidy šestiúhelníků
vrchol_x = obrazovka_x/2
vrchol_y = 2500/(velikost*2)
red = (255,0,0,100)
sed = (100,100,100)
orandzova = (255,165,0)
modra = (0,255,255)
#redPlayer = (255,0,0,254)

#mezera mezi šestiúhelníky
mezera = velikost/3
#o kolikatou radu se jedná
rada = 0
#ocislovani
ocislovani = 0
souradnice = 0
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
#šestiúhelník (vrchol-špička)
bod1 = (vrchol_x/4, vrchol_y)
bod2 = (vrchol_x/4 + math.ceil(math.sqrt((velikost*3) ** 2 - ((velikost*3) / 2) ** 2)),vrchol_y + ((velikost*3) / 2))
bod3 = (vrchol_x/4 + math.ceil(math.sqrt((velikost*3) ** 2 - ((velikost*3) / 2) ** 2)),vrchol_y + (velikost*3) + (velikost*3) / 2)
bod4 = (vrchol_x/4, vrchol_y + 2 * (velikost*3))
bod5 = (vrchol_x/4 - math.ceil(math.sqrt((velikost*3) ** 2 - ((velikost*3) / 2) ** 2)),vrchol_y + (velikost*3) + (velikost*3) / 2)
bod6 = (vrchol_x/4 - math.ceil(math.sqrt((velikost*3) ** 2 - ((velikost*3) / 2) ** 2)),vrchol_y + ((velikost*3) / 2))
#šestiúhelník (vrchol-přímka)
rada_odpovedi = 0
umisteni_odpovedi = 0
