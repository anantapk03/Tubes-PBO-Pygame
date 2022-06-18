import pygame
import random
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


asset = path.join(path.dirname(__file__), 'game_asset')
ledak = path.join(path.dirname(__file__), 'explosion')
sound = path.join(path.dirname(__file__), 'soundeffect')


# ambil gambar
background = pygame.image.load(path.join(asset, "starfield.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(asset, "spaceship.png")).convert()
# nyawa player
player_mini_img = pygame.transform.scale(player_img, (30, 20))
player_mini_img.set_colorkey(BLACK)
musuh_img = []
musuh_list = ['meteor5.png', 'meteor4.png', 'mete.png']
for img in musuh_list:
    musuh_img.append(pygame.image.load(path.join(asset, img)).convert())
pelor_img = pygame.image.load(path.join(asset, "pelor.png")).convert()
game_over_img = pygame.image.load(path.join(asset, "gameover.png")).convert()

# ambil sound
shoot_sound = pygame.mixer.Sound(path.join(sound, "tembakin.wav"))
ledakan_sound = []
for snd in ["Explosion.wav", "expl6.wav"]:
    ledakan_sound.append(pygame.mixer.Sound(path.join(sound, snd)))
pygame.mixer.music.load(path.join(sound, "song.mp3"))
pygame.mixer.music.set_volume(0.8)

# ledakan
ledakan_anim = {}
ledakan_anim['gede'] = []
ledakan_anim['kecil'] = []
ledakan_anim['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(ledak, filename)).convert()
    img.set_colorkey(BLACK)
    img_gede = pygame.transform.scale(img, (75, 75))
    ledakan_anim['gede'].append(img_gede)
    img_kecil = pygame.transform.scale(img, (32, 32))
    ledakan_anim['kecil'].append(img_kecil)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(ledak, filename)).convert()
    img.set_colorkey(BLACK)
    ledakan_anim['player'].append(img)
    
    

#inisiasi pygame dan buat window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tubes Game")
clock = pygame.time.Clock()


# cetak score 
font_name = pygame.font.match_font("arial")
def cetak_score(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop  = (x, y)
    surf.blit(text_surface, text_rect)

def newmassa():
    m = Massa()
    all_sprites.add(m)
    massa.add(m)
    
def gambar_shield(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def gambar_nyawa(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)
        
def show_go_screen():
    screen.blit(background, background_rect)
    cetak_score(screen, "Shooters", 64, WIDTH / 2, HEIGHT / 4)
    cetak_score(screen, "Tekan kiri dan kanan untuk menghindar, S untuk nembak", 16, WIDTH / 2, HEIGHT / 2)
    cetak_score(screen, "Tekan apa saja untuk mulai", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
show_go_screen()


class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 25
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
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
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
        
        
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_s]:
            self.tembak()
        self.rect.x += self.speedx
        if self.rect.right >  WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
    def tembak(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_delay:
            self.last_shoot = now
            peluru = Peluru(self.rect.centerx, self.rect.top)
            all_sprites.add(peluru)
            pelor.add(peluru)
            shoot_sound.play() 
            
    def hide(self):
        # hilang/sembunyikan sementara
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH/ 2, HEIGHT + 200)
        
class Massa(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig =  random.choice(musuh_img)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        self.speedy = random.randrange(2, 6)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()
        
    def rotasi(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            # lakukan rotasi
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center =  old_center 
        
    def update(self):
        self.rotasi()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 6)
        
class Peluru(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pelor_img
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

class Ledakan(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = ledakan_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(ledakan_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = ledakan_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


all_sprites = pygame.sprite.Group()
massa = pygame.sprite.Group()
pelor = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(8):
    newmassa()   
    
score = 0

pygame.mixer.music.play(loops = -1)
# game loop
game_over = False
running = True
while running:
    if game_over:
        screen.blit(game_over_img, (0, 0))
        game_over = False
        all_sprites = pygame.sprite.Group()
        massa = pygame.sprite.Group()
        pelor = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(8):
            newmassa()
        score = 0
    # keep loop running at the right speed
    clock.tick(FPS)
    # proses input (events)
    for event in pygame.event.get():
        # kalo close game
        if event.type == pygame.QUIT:
            running = False
            
    # update
    all_sprites.update()
    
    # cek ketika player menembak
    kena = pygame.sprite.groupcollide(massa, pelor, True, True)
    for hit in kena:
        score += 50 - hit.radius
        random.choice(ledakan_sound).play()
        expl = Ledakan(hit.rect.center, 'gede')
        all_sprites.add(expl)
        newmassa()
    
    
    # cek ketika player mengenai musuh
    nabrak = pygame.sprite.spritecollide(player, massa, False, pygame.sprite.collide_circle)
    for hit in nabrak:
        player.shield -= player.radius * 2
        expl = Ledakan(hit.rect.center, 'kecil')
        all_sprites.add(expl)
        newmassa()
        if player.shield <= 0:
            death_explosion = Ledakan(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            player.hide()
            player.lives -= 1
            player.shield = 100
            #running = False
        
        # jika nyawa player abis 
        if player.lives < 1 and death_explosion.alive():
            running = False
            screen.blit(game_over_img, (0, 0))
            
    
    
    # render gamse
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    cetak_score(screen, str(score), 18, WIDTH / 2, 10)
    gambar_shield(screen, 5, 5, player.shield)
    gambar_nyawa(screen, WIDTH - 100, 5, player.lives, player_mini_img)
    # flip display
    pygame.display.flip()
    
pygame.quit()