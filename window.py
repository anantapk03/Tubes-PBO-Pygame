import pygame
from os import path


#buat warna bg
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

WIDTH  = 360
HEIGHT = 480
FPS = 60

#inisiasi pygame dan buat window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tubes Game")
clock = pygame.time.Clock()

# load asset files
asset = path.join(path.dirname(__file__), 'img')

# ambil gambar
background = pygame.image.load(path.join(asset, "starfield.png")).convert()
background_rect = background.get_rect()
peluru_img = pygame.image.load(path.join(asset, "laserRed16.png")).convert()
player_img = pygame.image.load(path.join(asset, "playerShip1_orange.png")).convert() 
meteor_img = []
meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 'meteorBrown_small1.png']
for img in meteor_list:
    meteor_img.append(pygame.image.load(path.join(asset, img)).convert())
    
all_sprites = pygame.sprite.Group()
bullet = pygame.sprite.Group()
meteor = pygame.sprite.Group()


