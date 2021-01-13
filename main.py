import pygame
import para
import math
import numpy

pygame.init()
screen = pygame.display.set_mode((para.obrazovka_x, para.obrazovka_y))
cas = pygame.time.Clock()

class Sestiuhelnik(pygame.sprite.Sprite):
    def __init__(self):
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
        self.barva = (255-para.bc,0,0)
        self.DEFIbarva = self.barva
        #self.barva = (255,0,0)
        #důležité pro souradnce
        self.oznaceni = para.bc
        self.cislo = [para.ocislovani, para.rada]
        self.podminka = [None, None, None] #levá strana, dolní strana, pravá strana
        self.odecteni_y = self.bod6[1] - self.bod1[1]  #polovina horního trojúhelníku v šestiúhelníku v y
        self.odecteni_x = (self.bod2[0] - self.bod6[0])/2 #polovina horního trojúhelníku v šestiúhelníku v x
        #print(int(self.bod6[0]))
        #self.surf = pygame.draw.rect(screen, (255,255,0) ,pygame.Rect(int(self.bod6[0]),int(self.bod6[1]),int(self.bod2[0]),int(self.bod5[1])))
        #self.rect = self.surf.get_rect()
        #print(self.cislo)
        if para.rada == para.zadano:
            self.podminka[1] = True
            #print("^prostřední strana")
        if para.rada%2 == 0 and para.ocislovani == -math.floor((para.rada-1)/2):
            self.podminka[2] = True
            #print("^pravá strana")
        if para.rada % 2 != 0 and para.ocislovani - 1 == -math.floor((para.rada-1)/2):
            self.podminka[2] = True
            #print("^pravá strana")
        if para.ocislovani >= para.rada/2:
            para.rada += 1
            para.ocislovani = -math.floor(para.rada/2)
            self.podminka[0] = True
            #print("^levá strana" )
        #print(self.podminka)
        para.ocislovani += 1
        para.bc += 1

        #print(self.cislo)
    def update(self, pos, pixel):
        for entity in sestiuhelniky:
            if (pos[0] >= self.bod6[0] and pos[0] <= self.bod2[0]) and pos[1] >= self.bod1[1] and pos[1] <= self.bod4[1] and pixel == self.barva:   #čtverec uprostřed
                #sestiuhelniky_zabrane_O.add(sestiuhelnik)
                if para.zacinajici_hrac == True:
                    self.DEFIbarva = (255-math.floor(self.oznaceni/2),165-math.floor(self.oznaceni/2),0,255)
                    hracO.update(self.podminka[0],self.podminka[1],self.podminka[2])
                    #sestiuhelniky_zabrane_O.add(entity)
                if para.zacinajici_hrac == False:
                    self.DEFIbarva = (0,255-math.floor(self.oznaceni/2) ,255-math.floor(self.oznaceni/2), 255)
                    #sestiuhelniky_zabrane_M.add(entity)
                    hracM.update(self.podminka[0], self.podminka[1], self.podminka[2])
                print(para.zacinajici_hrac)
                    #print(self.podminka)
            #elif pos[1] >= self.bod1[1] and pos[1] <= self.bod5[1]:
        #self.kill()
        #print("OwO")

class O_hrac(pygame.sprite.Sprite): #orandzovy hrac
    def __init__(self):
        super(O_hrac, self).__init__()
        self.leva_s = False
        self.prava_s = False
        self.dolni_s = False
        self.bod1 = para.bod1
        self.bod2 = para.bod2
        self.bod3 = para.bod3
        self.bod4 = para.bod4
        self.bod5 = para.bod5
        self.bod6 = para.bod6
    def update(self, leva, dolni,prava):
        if leva == True:
            self.leva_s = True
        if dolni == True:
            self.dolni_s = True
        if prava == True:
            self.prava_s = True
         #DODĚLAT PODMÍNKY
        if self.leva_s and self.prava_s and self.dolni_s:
            print("Orandzovy KONEC")

class M_hrac(pygame.sprite.Sprite): #modrý hrac
    def __init__(self):
        super(M_hrac, self).__init__()
        self.leva_s = False
        self.prava_s = False
        self.dolni_s = False
        self.bod1 = (para.bod1[0]+para.vrchol_x*0.75+para.obrazovka_x/4+para.velikost*5,para.bod1[1])
        self.bod2 = (para.bod2[0]+para.vrchol_x*0.75+para.obrazovka_x/4+para.velikost*5,para.bod2[1])
        self.bod3 = (para.bod3[0]+para.vrchol_x*0.75+para.obrazovka_x/4+para.velikost*5,para.bod3[1])
        self.bod4 = (para.bod4[0]+para.vrchol_x*0.75+para.obrazovka_x/4+para.velikost*5,para.bod4[1])
        self.bod5 = (para.bod5[0]+para.vrchol_x*0.75+para.obrazovka_x/4+para.velikost*5,para.bod5[1])
        self.bod6 = (para.bod6[0]+para.vrchol_x*0.75+para.obrazovka_x/4+para.velikost*5,para.bod6[1])
    def update(self, leva, dolni,prava):
        #print(leva)
        if leva == True:
            self.leva_s = True
        if dolni == True:
            self.dolni_s = True
        if prava == True:
            self.prava_s = True
        # DODĚLAT PODMÍNKY
        if self.leva_s and self.prava_s and self.dolni_s:
            print("Modry KONEC")
class Otazka (pygame.sprite.Sprite):
    def __init__(self):
        super(Otazka, self).__init__()

        self.bod1 = ((para.vrchol_x / 10) - para.mezera, ((para.velikost * para.rada)*(para.velikost*1.25)))
        self.bod2 = ((para.vrchol_x / 6 - para.mezera), (((para.velikost * para.rada)*(para.velikost*1.25)) + para.velikost *2))
        self.bod3 = ((para.vrchol_x / 2.75 + para.velikost * 10 + para.vrchol_x - para.mezera), (((para.velikost * para.rada)*(para.velikost*1.25)) + para.velikost *2))
        self.bod4 = (((para.vrchol_x / 10)*19), (((para.velikost * para.rada)*(para.velikost*1.25))))
        self.bod5 = ((para.vrchol_x / 2.75 + para.velikost * 10 + para.vrchol_x - para.mezera),(((para.velikost * para.rada)*(para.velikost*1.25)) - para.velikost *2))
        self.bod6 = ((para.vrchol_x / 6 - para.mezera), (((para.velikost * para.rada)*(para.velikost*1.25)) - para.velikost *2))
        #verze na automatické zobrazení pomocí počtu rad - NEMAZAT
        '''
        self.bod1 = ((para.vrchol_x / 10) - para.mezera, ((para.velikost ** para.zadano) * (para.zadano * para.velikost)))
        self.bod2 = ((para.vrchol_x / 6 - para.mezera), (((para.velikost ** para.zadano) * (para.zadano * para.velikost)) + para.velikost *2))
        self.bod3 = ((para.vrchol_x / 2.75 + para.velikost * 10 + para.vrchol_x - para.mezera), (((para.velikost ** para.zadano) * (para.zadano * para.velikost)) + para.velikost *2))
        self.bod4 = (((para.vrchol_x / 10)*19), ((para.velikost ** para.zadano) * (para.zadano * para.velikost)))
        self.bod5 = ((para.vrchol_x / 2.75 + para.velikost * 10 + para.vrchol_x - para.mezera),(((para.velikost ** para.zadano) * (para.zadano * para.velikost)) - para.velikost *2))
        self.bod6 = ((para.vrchol_x / 6 - para.mezera), (((para.velikost ** para.zadano) * (para.zadano * para.velikost)) - para.velikost *2))
        '''
    def update(self):
        pass
        #sem pokud možno script na otázky

ADDSESTIUHELNIK = pygame.USEREVENT + 1
pygame.time.set_timer(ADDSESTIUHELNIK,10)
sestiuhelnik = Sestiuhelnik()
sestiuhelniky = pygame.sprite.Group()
sestiuhelniky_zabrane_O = pygame.sprite.Group()
sestiuhelniky_zabrane_M = pygame.sprite.Group()
hracM = M_hrac()
hracO = O_hrac()
pole_otazky = Otazka()

while para.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            para.running = False
        elif event.type == para.KEYDOWN:
            if event.key == para.K_ESCAPE:
                para.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cas.tick(2000)
            print("click")
            pos = pygame.mouse.get_pos()
            pixel = para.obrazovka.get_at((pos))
            #obstacle = pygame.mask.from_surface(surf)
            #print(sestiuhelniky)
            for entity in sestiuhelniky:
                if pixel == entity.DEFIbarva:
                    if entity.DEFIbarva[1] == 0:
                        para.premena2 = para.zacinajici_hrac
                        para.zacinajici_hrac = para.premena
                        para.premena = para.premena2
                        sestiuhelniky.update(pos, pixel)
                        pole_otazky.update()#DOKONCIT
                        para.zacatek = False
                        if para.zacinajici_hrac == True:
                            sestiuhelniky_zabrane_O.add(entity)
                        if para.zacinajici_hrac == False:
                            sestiuhelniky_zabrane_M.add(entity)
                        print(sestiuhelniky_zabrane_M)
            #hracO.update(sestiuhelniky_zabrane_O)
            #hracM.update(sestiuhelniky_zabrane_M)
            #sestiuhelniky_zabrane.update()

            #sestiuhelniky = ""
            #sestiuhelniky = pygame.sprite.Group()
                
            #print(pos)
            #print(pixel)
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
        pygame.draw.polygon(para.obrazovka, entity.DEFIbarva, (entity.bod1, entity.bod2, entity.bod3, entity.bod4, entity.bod5, entity.bod6))
        #pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(int(entity.bod6[0]), int(entity.bod6[1]),math.ceil(math.sqrt(para.velikost ** 2 - (para.velikost / 2) ** 2))*2, para.velikost))
    if para.zacinajici_hrac == False:
        barva = para.sed
        barva2 = para.orandzova
        barva3 = barva2
    else:
        barva = para.modra
        barva2 = para.sed
        barva3 = barva
    pygame.draw.polygon(para.obrazovka, barva,(hracM.bod1, hracM.bod2, hracM.bod3, hracM.bod4, hracM.bod5, hracM.bod6))
    pygame.draw.polygon(para.obrazovka, barva2,(hracO.bod1, hracO.bod2, hracO.bod3, hracO.bod4, hracO.bod5, hracO.bod6))
    if para.zacatek == True:
        barva3 = para.sed
    pygame.draw.polygon(para.obrazovka, barva3,(pole_otazky.bod1, pole_otazky.bod2, pole_otazky.bod3, pole_otazky.bod4, pole_otazky.bod5, pole_otazky.bod6))

    #pygame.display.flip()

    pygame.display.flip()
    cas.tick(100)
pygame_quit = pygame.quit()

