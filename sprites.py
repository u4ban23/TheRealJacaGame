from jaca import *
from somerek import *

class Sprites:
    def __init__(self, screen=None):
        self.screen = screen
        self.jaca = Jaca(self.screen)
        self.somerek = Piwko(self.screen)
        self.allSprites = pygame.sprite.Group()
        self.allSprites.add(self.jaca)
        self.allSprites.add(self.somerek)
        self.somerek_can_blit = True
        
    def blit_sprites(self, event):
        self.jaca.blit()
        if not self.jaca.piwko_picked_up and self.somerek_can_blit:
            self.somerek.blit()
            self.somerek_can_blit = False
        self.allSprites.update()

    def move_sprites(self):
        self.jaca.movement()
        self.jaca.border()
        
    def mechanic(self, event):
        self.jaca.pickUpPiwko(event)
        self.jaca.wychlej(event)
        # print(self.jaca.piwko_picked_up)
        # print(self.somerek.image_count, self.jaca.piwko_picked_up)