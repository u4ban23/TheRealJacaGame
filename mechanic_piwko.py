import pygame
from sprites import *



class Mechanic_PickUp:
    def __init__(self):
        self.s = Sprites()
        self.piwko_picked_up = False
      
    

        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_e:
        #             self.piwko_picked_up = not self.piwko_picked_up
        #             if self.piwko_picked_up:
        #                 self.s.somerek.rect.x = self.s.jaca.rect.x
        #                 self.s.somerek.rect.y = self.s.jaca.rect.y
        #                 print('true')
        #             else:
        #                 print('false')