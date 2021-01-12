import pygame
import para
import math

pygame.init()
screen = pygame.display.set_mode((para.obrazovka_x, para.obrazovka_y))

class Sestiuhelnik(pygame.sprite.Sprite):
    def __init__(self, false=None):
        super(Sestiuhelnik, self).__init__()
        if para.rada %2 == 0:
            self.bod1 = (para.vrchol_x - (para.odsazeni_x * para.ocislovani) + para.velikost, para.vrchol_y + para.odsazeni_y * para.rada)
            self.bod2 = (para.vrchol_x + math.ceil(math.sqrt(para.velikost ** 2 - (para.velikost / 2) ** 2)) - (para.odsazeni_x * para.ocislovani) + para.velikost,para.vrchol_y + (para.velikost / 2) + para.odsazeni_y * para.rada)
            self.bod3 = (para.vrchol_x + math.ceil(math.sqrt(para.velikost ** 2 - (para.velikost / 2) ** 2)) - (para.odsazeni_x * para.ocislovani) + para.velikost,para.vrchol_y + para.velikost + para.velikost / 2 + para.odsazeni_y * para.rada)
            self.bod4 = (para.vrchol_x - (para.odsazeni_x * para.ocislovani) + para.velikost,para.vrchol_y + 2 * para.velikost + para.odsazeni_y * para.rada)
            self.bod5 = (para.vrchol_x - math.ceil(math.sqrt(para.velikost ** 2 - (para.velikost / 2) ** 2)) - (para.odsazeni_x * para.ocislovani) + para.velikost,para.vrchol_y + para.velikost + para.velikost / 2 + para.odsazeni_y * para.rada)
            self.bod6 = (para.vrchol_x - math.ceil(math.sqrt(para.velikost ** 2 - (para.velikost / 2) ** 2)) - (para.odsazeni_x * para.ocislovani) + para.velikost,para.vrchol_y + (para.velikost / 2) + para.odsazeni_y * para.rada)
        else:
            self.bod1 = (para.vrchol_x - (para.odsazeni_x*para.ocislovani) + 2*para.velikost, para.vrchol_y + para.odsazeni_y*para.rada)
            self.bod2 = (para.vrchol_x + math.ceil(math.sqrt(para.velikost ** 2 - (para.velikost / 2) ** 2)) - (para.odsazeni_x*para.ocislovani) + 2*para.velikost,para.vrchol_y + (para.velikost / 2) + para.odsazeni_y*para.rada)
            self.bod3 = (para.vrchol_x + math.ceil(math.sqrt(para.velikost ** 2 - (para.velikost / 2) ** 2)) - (para.odsazeni_x*para.ocislovani) + 2*para.velikost,para.vrchol_y + para.velikost + para.velikost / 2 + para.odsazeni_y*para.rada)
            self.bod4 = (para.vrchol_x - (para.odsazeni_x*para.ocislovani) + 2*para.velikost, para.vrchol_y + 2 * para.velikost + para.odsazeni_y*para.rada)
            self.bod5 = (para.vrchol_x - math.ceil(math.sqrt(para.velikost ** 2 - (para.velikost / 2) ** 2)) - (para.odsazeni_x*para.ocislovani) + 2*para.velikost,para.vrchol_y + para.velikost + para.velikost / 2 + para.odsazeni_y*para.rada)
            self.bod6 = (para.vrchol_x - math.ceil(math.sqrt(para.velikost ** 2 - (para.velikost / 2) ** 2)) - (para.odsazeni_x*para.ocislovani) + 2*para.velikost,para.vrchol_y + (para.velikost / 2) + para.odsazeni_y*para.rada)
        #self.barva = (255-para.bc,0,0)
        self.barva = (255,0,0)
        self.oznaceni = para.bc
        self.cislo = [para.ocislovani, para.rada]
        if para.ocislovani >= para.rada/2:
            para.rada += 1
            para.ocislovani = -math.floor(para.rada/2)
        para.ocislovani += 1
        para.bc += 1

        print(self.cislo)
    def update(self):
        self.barva = (255,255,255,255)
        #self.kill()
        print("OwO")
    def collidepoint(self, sestiuhelniky):
        #if pygame.sprite.spritecollide(self, sestiuhelniky, False):
            self.barva = (255, 255, 255, 255)

ADDSESTIUHELNIK = pygame.USEREVENT + 1
pygame.time.set_timer(ADDSESTIUHELNIK,1)
sestiuhelnik = Sestiuhelnik()
sestiuhelniky = pygame.sprite.Group()

while para.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            para.running = False
        elif event.type == para.KEYDOWN:
            if event.key == para.K_ESCAPE:
                para.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pixel = para.obrazovka.get_at((pos))
            obstacle = pygame.mask.from_surface(surf)
            print(sestiuhelniky)
            if pixel == para.red:

                sestiuhelniky.update()
                
                #sestiuhelniky = ""
                #sestiuhelniky = pygame.sprite.Group()
                
                print(pos)
                print(pixel)
                '''
            if sestiuhelnik.collidepoint(pos):
                print(pos)
                print(pixel)
                '''

        elif event.type == ADDSESTIUHELNIK and para.rada <= para.zadano:
            novy_sestiuhelnik = Sestiuhelnik()
            sestiuhelniky.add(novy_sestiuhelnik)


    #zkušební střední polygon
    '''
    bod1 = (para.vrchol_x, para.vrchol_y)
    bod2 = (para.vrchol_x+math.ceil(math.sqrt(para.velikost**2-(para.velikost/2)**2)), para.vrchol_y+(para.velikost/2))
    bod3 = (para.vrchol_x+math.ceil(math.sqrt(para.velikost**2-(para.velikost/2)**2)), para.vrchol_y+para.velikost+ para.velikost/2)
    bod4 = (para.vrchol_x, para.vrchol_y+ 2*para.velikost)
    bod5 = (para.vrchol_x-math.ceil(math.sqrt(para.velikost**2-(para.velikost/2)**2)), para.vrchol_y+para.velikost+ para.velikost/2)
    bod6 = (para.vrchol_x-math.ceil(math.sqrt(para.velikost**2-(para.velikost/2)**2)), para.vrchol_y+(para.velikost/2))
    pygame.draw.polygon(para.obrazovka, (255,255,255), (bod1, bod2, bod3, bod4, bod5, bod6))
    '''
    #if sestiuhelnik.collidepoint(pygame.mouse.get_pos()):
    #Sestiuhelnik.update()
    #maska = pygame.mask.from_threshold(pygame.display, para.red)
    #pygame.maska.update()
    screen.fill((0,0,0))
    surf = pygame.Surface((50, 50))
    surf.fill((255,255,255))
    rect = surf.get_rect()
    surf_center = (
        (para.obrazovka_x - surf.get_width())/2,
        (para.obrazovka_y - surf.get_height())/2,
    )
    for entity in sestiuhelniky:
        pygame.draw.polygon(para.obrazovka, entity.barva, (entity.bod1, entity.bod2, entity.bod3, entity.bod4, entity.bod5, entity.bod6))
    #pygame.display.flip()

    pygame.display.flip()
pygame_quit = pygame.quit()

