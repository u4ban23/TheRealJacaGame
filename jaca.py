import pygame
from settings import *
from somerek import *
from rowerek import *

class Jaca(pygame.sprite.Sprite):
    def __init__(self, screen=None):
        super().__init__()
        self.screen = screen
        self.images = [pygame.image.load('images/Jaca.png'),
                       pygame.image.load('images/Jaca-left.png'),
                       pygame.image.load('images/Jaca-right.png')]
        
        self.image_count = 0
        self.current_image = self.images[self.image_count]
        self.rect = self.current_image.get_rect()
        self.speed = 5
        self.rect.topleft = (100, 200)
        self.piwko_picked_up = False
        self.somerek = Piwko(self.screen)
        self.rowerek = Rower(self.screen)
        self.direction = 0

    def blit(self):
        self.screen.blit(self.images[self.image_count], self.rect)
        
        if self.piwko_picked_up:
            if self.direction == 0:
                self.somerek.rect.topleft = self.rect.topleft
                self.somerek.rect.y = self.rect.y + 170
            elif self.direction == 1:
                self.somerek.rect.topleft = self.rect.topleft
                self.somerek.rect.x += 170
                self.somerek.rect.y += 140
                
            elif self.direction == -1:
                self.somerek.rect.topleft = self.rect.topleft
                self.somerek.rect.y += 150
                self.somerek.rect.x += 10
            self.somerek.blit()
        else:
            self.somerek.blit()

        # pygame.draw.rect(self.screen, (255, 0, 0, 100), self.rect, 2)  ## hitbox
        
    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.image_count = 0
            self.direction = 0

        elif keys[pygame.K_s]:
            self.rect.y += self.speed
            self.image_count = 0
            self.direction = 0

        elif keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.image_count = 1
            self.direction = -1

        elif keys[pygame.K_d]:
            self.rect.x += self.speed
            self.image_count = 2
            self.direction = 1

        else:
            self.image_count = 0
            self.direction = 0

    def border(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= WINDOW_WIDTH - self.rect.width:
            self.rect.x = WINDOW_WIDTH - self.rect.width

        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= WINDOW_HEIGHT - self.rect.height:
            self.rect.y = WINDOW_HEIGHT - self.rect.height

    def pickUpAvailable(self):
        return self.somerek.rect.colliderect(self.rect)
    
    def naRowerekAvaible(self):
        return self.rowerek.rect.colliderect(self.rect)
        
    def pickUpPiwko(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e and self.pickUpAvailable():
                self.piwko_picked_up = not self.piwko_picked_up
                if self.piwko_picked_up:
                    pass
            
    def wychlej(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f and self.piwko_picked_up:
                self.somerek.image_count += 1
                self.somerek.current_image = self.somerek.images[self.somerek.image_count]
                if self.somerek.image_count > 2:
                    self.somerek.image_count = 2

        ### actions after drink
        if self.somerek.image_count == 1:
            self.speed = 7
        elif self.somerek.image_count == 2:
            self.speed = 10
        else:
            self.speed = 5
                
    def naRower(self,event):
        # print(self.naRowerekAvaible, self.pickUpAvailable, self.piwko_picked_up)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e and self.naRowerekAvaible and not self.pickUpAvailable and not self.piwko_picked_up:
                self.rowerek.rect.x = self.rect.x
                self.rowerek.rect.y = self.rect.y

