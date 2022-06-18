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

score = 0

# load asset files
asset = path.join(path.dirname(__file__), 'img')
sound = path.join(path.dirname(__file__), 'snd')

# ambil gambar
background = pygame.image.load(path.join(asset, "starfield.png")).convert()
background_rect = background.get_rect()
peluru_img = pygame.image.load(path.join(asset, "laserRed16.png")).convert()
player_img = pygame.image.load(path.join(asset, "playerShip1_orange.png")).convert() 
meteor_img = []
meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 'meteorBrown_small1.png']
for img in meteor_list:
    meteor_img.append(pygame.image.load(path.join(asset, img)).convert())
player_mini_img = pygame.transform.scale(player_img, (30, 20))
player_mini_img.set_colorkey(BLACK)
game_over_img = pygame.image.load(path.join(asset, "playerShip1_orange.png")).convert()



# ledakan sound
ledakan_sound = []
for snd in ["expl3.wav", "expl6.wav"]:
    ledakan_sound.append(pygame.mixer.Sound(path.join(sound, snd)))
pygame.mixer.music.load(path.join(sound, "song.mp3"))
pygame.mixer.music.set_volume(0.8)

pygame.mixer.music.play(loops = -1)

# ledakan
ledakan_anim = {}
ledakan_anim['gede'] = []
ledakan_anim['kecil'] = []
ledakan_anim['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(asset, filename)).convert()
    img.set_colorkey(BLACK)
    img_gede = pygame.transform.scale(img, (75, 75))
    ledakan_anim['gede'].append(img_gede)
    img_kecil = pygame.transform.scale(img, (32, 32))
    ledakan_anim['kecil'].append(img_kecil)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(asset, filename)).convert()
    img.set_colorkey(BLACK)
    ledakan_anim['player'].append(img)
    

all_sprites = pygame.sprite.Group()
bullet = pygame.sprite.Group()
meteor = pygame.sprite.Group()


