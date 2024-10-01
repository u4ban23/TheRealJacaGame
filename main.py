import sys
from settings import *
import pygame
import sprites
from background import *
import initMechanic



pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.sprites = sprites.Sprites(self.screen)
        self.clock = pygame.time.Clock()
        self.background = Background(self.screen)
        self.mechanic = initMechanic.Mechanic(self.screen)


    def upload(self, event):
        Background(self.screen)
        self.sprites.blit_sprites(event)
        self.sprites.move_sprites()

    def uploadMechanic(self, event):
        self.mechanic.initMechanicPiwko(event)

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.uploadMechanic(event)

            self.upload(event)
            
            self.clock.tick(FPS)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.game_loop()