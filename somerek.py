import pygame
from settings import *
from jaca import *

class Piwko(pygame.sprite.Sprite):
    def __init__(self, screen=None):
        super().__init__()
        self.screen = screen
        self.image_count = 0
        self.images = [pygame.image.load('images/somerek.png'),
                      pygame.image.load('images/somerek_polwychlany.png'),
                      pygame.image.load('images/somerek_wychlany.png')]
        
        self.current_image = self.images[self.image_count]
        
        self.rect = self.images[self.image_count].get_rect()
        self.rect.topleft = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
        
    def blit(self):
        self.screen.blit(self.current_image, self.rect)
        print(self.image_count)
        # pygame.draw.rect(self.screen, (0, 255, 0, 100), self.rect, 2)  ## hitbox

    def update_image(self):
        self.current_image = self.images[self.image_count]
        self.rect = self.current_image.get_rect()
        self.rect.topleft = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

    