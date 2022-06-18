import pygame
from window import *

class Peluru(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = peluru_img
        self.image.set_colorkey(BLACK)
        #self.image = pygame.Surface((10, 20))
        #self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        
    def update(self):
        self.rect.y += self.speedy
        # jika peluru mengenai musuh
        if self.rect.bottom < 0:
            self.kill()