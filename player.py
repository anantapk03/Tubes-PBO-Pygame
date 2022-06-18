import pygame 
import window 
from peluru import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(window.player_img, (50, 38))
        self.image.set_colorkey(window.BLACK)
        self.rect = self.image.get_rect()
        self.radius = 25
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = window.WIDTH / 2
        self.rect.bottom = window.HEIGHT - 10
        self.speedx = 0
        self.shield = 100
        self.shoot_delay = 250
        self.last_shoot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def update(self):
        # unhidden if hidden
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = window.WIDTH / 2
            self.rect.bottom = window.HEIGHT - 10
        
        
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_s]:
            self.tembak()
        self.rect.x += self.speedx
        if self.rect.right >  window.WIDTH:
            self.rect.right = window.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    
    def tembak(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_delay:
            self.last_shoot = now
            peluru = Peluru(self.rect.centerx, self.rect.top)
            window.all_sprites.add(peluru)
            bullet.add(peluru)
    

    def hide(self):
        # hilang/sembunyikan sementara
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (window.WIDTH/ 2, window.HEIGHT + 200)



