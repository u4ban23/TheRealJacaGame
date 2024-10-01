import pygame
from mechanic.piwkoMechanic import *
from mechanic.rowerMechanic import *

class Mechanic:
    def __init__(self, screen):
        self.screen = screen
        self.mechanicPiwko = PiwkoMechanic(self.screen)

    def initMechanicPiwko(self, event):
        self.mechanicPiwko.pickUpAvailable()
        self.mechanicPiwko.pickUpPiwko(event)
        self.mechanicPiwko.wychlej(event)