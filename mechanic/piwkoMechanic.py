import pygame
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sprites import Sprites

class PiwkoMechanic:
    def __init__(self, screen, jaca, somerek):
        self.screen = screen
        self.sprites = Sprites(self.screen)
        self.somerek = somerek
        self.jaca = jaca
        self.piwko_picked_up = False

    def pickUpAvailable(self):
        if self.somerek.rect.colliderect(self.jaca.rect):
            print('działa kod do hb piwka')
        return self.somerek.rect.colliderect(self.jaca.rect)
    
    def pickUpPiwko(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e and self.pickUpAvailable():
                self.piwko_picked_up = not self.piwko_picked_up
                self.jaca.piwko_picked_up = self.piwko_picked_up
                if self.piwko_picked_up:
                    pass
            
    def wychlej(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f and self.piwko_picked_up:
                self.somerek.image_count += 1
                if self.somerek.image_count > 2:
                    self.somerek.image_count = 2
                self.somerek.update_image()
                if self.somerek.image_count == 1:
                    self.jaca.speed = 7
                elif self.somerek.image_count == 2:
                    self.jaca.speed = 10
                else:
                    self.jaca.speed = 5
                