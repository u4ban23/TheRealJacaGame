import pygame

class Rower(pygame.sprite.Sprite):
    def __init__(self, screen=None):
        super().__init__()
        self.screen = screen
        self.images = [pygame.image.load('images/rower-animation/rower-1.png'),
                       pygame.image.load('images/rower-animation/rower-2.png'),
                       pygame.image.load('images/rower-animation/rower-3.png'),
                       pygame.image.load('images/rower-animation/rower-4.png')]
        self.image_count = 0
        self.current_image = self.images[self.image_count]
        self.rect = self.current_image.get_rect()
        self.rect.topleft = (700,500)


    def blit(self):
        self.screen.blit(self.current_image, self.rect)

    