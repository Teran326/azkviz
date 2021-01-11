import pygame
import para
import math
pygame.init()
ADDSESTIUHELNIK = pygame.USEREVENT

class Sestiuhelnik():
    def __init__(self):
        super(Sestiuhelnik, self).__init__()
        self.bod1 = (para.vrchol_x, para.vrchol_y)
        self.bod2 = (para.vrchol_x + math.ceil(math.sqrt(para.velikost ** 2 - (para.velikost / 2) ** 2)),para.vrchol_y + (para.velikost / 2))
        self.bod3 = (para.vrchol_x + math.ceil(math.sqrt(para.velikost ** 2 - (para.velikost / 2) ** 2)),para.vrchol_y + para.velikost + para.velikost / 2)
        self.bod4 = (para.vrchol_x, para.vrchol_y + 2 * para.velikost)
        self.bod5 = (para.vrchol_x - math.ceil(math.sqrt(para.velikost ** 2 - (para.velikost / 2) ** 2)),para.vrchol_y + para.velikost + para.velikost / 2)
        self.bod6 = (para.vrchol_x - math.ceil(math.sqrt(para.velikost ** 2 - (para.velikost / 2) ** 2)),para.vrchol_y + (para.velikost / 2))
        self.cislo = para.ocislovani
        para.ocislovani += 1
    def update(self):
        pygame.draw.polygon(para.obrazovka, para.blue, (self.bod1, self.bod2, self.bod3, self.bod4, self.bod5, self.bod6))

while para.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            para.running = False
        elif event.type == para.KEYDOWN:
            if event.key == para.K_ESCAPE:
                para.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
        elif event.type == ADDSESTIUHELNIK:
            jeden = Sestiuhelnik(para.rada, para.ocislovani)
    '''
    bod1 = (para.vrchol_x, para.vrchol_y)
    bod2 = (para.vrchol_x+math.ceil(math.sqrt(para.velikost**2-(para.velikost/2)**2)), para.vrchol_y+(para.velikost/2))
    bod3 = (para.vrchol_x+math.ceil(math.sqrt(para.velikost**2-(para.velikost/2)**2)), para.vrchol_y+para.velikost+ para.velikost/2)
    bod4 = (para.vrchol_x, para.vrchol_y+ 2*para.velikost)
    bod5 = (para.vrchol_x-math.ceil(math.sqrt(para.velikost**2-(para.velikost/2)**2)), para.vrchol_y+para.velikost+ para.velikost/2)
    bod6 = (para.vrchol_x-math.ceil(math.sqrt(para.velikost**2-(para.velikost/2)**2)), para.vrchol_y+(para.velikost/2))
    '''
    Sestiuhelnik()
    Sestiuhelnik.update()
    pygame.display.flip()
    pygame.display.update()
pygame.quit()