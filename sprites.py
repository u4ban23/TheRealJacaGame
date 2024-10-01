from jaca import *
from somerek import *
from rowerek import *

class Sprites:
    def __init__(self, screen=None):
        self.screen = screen
        self.jaca = Jaca(self.screen)
        self.rowerek = Rower(self.screen)
        self.somerek = Piwko(self.screen)

        self.allSprites = pygame.sprite.Group()
        self.allSprites.add(self.jaca)
        self.allSprites.add(self.somerek)
        self.allSprites.add(self.rowerek)
        self.somerek_can_blit = True
        
    def blit_sprites(self, event):
        self.jaca.blit()
        self.rowerek.blit()
        if not self.jaca.piwko_picked_up and self.somerek_can_blit:
            self.somerek.blit()
            self.somerek_can_blit = False
        self.allSprites.update()

    def move_sprites(self):
        self.jaca.movement()
        self.jaca.border()
        

