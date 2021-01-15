import math
import random
from src import para
import pickle


class Vyber:
    def __init__(self):
        self.spatne = ["", "", ""]
        self.reading = pickle.load(open("src/qna.dat", "rb"))
        self.answer = math.floor(random.randint(0, len(self.reading)-1))
        self.a = self.answer
        self.odpoved = self.reading[self.answer][1]
        self.otazka = self.reading[self.answer][0]
        self.rozmery = [para.obrazovka_x/100 + para.obrazovka_x/40, para.obrazovka_x/4 + para.obrazovka_x/40,
                        para.vrchol_x + para.obrazovka_x/40,
                        para.obrazovka_x - para.obrazovka_x/100 - 200 - para.obrazovka_x/40]

    def init(self):
        for j in range(3):
            self.spatne[j] = self.reading[math.floor(random.randint(0, len(self.reading) - 1))][1]
            while self.spatne[j] == self.odpoved:
                self.spatne[j] = self.reading[math.floor(random.randint(0, len(self.reading) - 1))][1]
