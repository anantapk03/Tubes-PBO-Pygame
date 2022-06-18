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

# load asset files
asset = path.join(path.dirname(__file__), 'img')

# ambil gambar
background = pygame.image.load(path.join(asset, "starfield.png"))
background_rect = background.get_rect()
peluru_img = pygame.image.load(path.join(asset, "laserRed16.png"))

#inisiasi pygame dan buat window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tubes Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
peluru = pygame.sprite.Group()

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
            
# Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()