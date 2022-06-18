import pygame
from player import Player
from window import *
from meteor import Meteor
from menu import *
import random
from ledakan import Ledakan
from nyawa import *

Menu.show_go_screen()

player = Player()
all_sprites.add(player)


for i in range(8):
    m = Meteor()
    all_sprites.add(m)
    meteor.add(m)


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

    # cek ketika player menembak
    kena = pygame.sprite.groupcollide(meteor, bullet, True, True)
    for hit in kena:
        score += 50 - hit.radius
        random.choice(ledakan_sound).play()
        expl = Ledakan(hit.rect.center, 'gede')
        all_sprites.add(expl)
        m = Meteor()
        all_sprites.add(m)
        meteor.add(m)


    # cek ketika player mengenai musuh
    nabrak = pygame.sprite.spritecollide(player, meteor, False, pygame.sprite.collide_circle)
    for hit in nabrak:
        player.shield -= player.radius * 2
        expl = Ledakan(hit.rect.center, 'kecil')
        all_sprites.add(expl)
        m = Meteor()
        all_sprites.add(m)
        meteor.add(m)

        if player.shield <= 0:
            death_explosion = Ledakan(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            player.hide()
            player.lives -= 1
            player.shield = 100

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    Nyawa.gambar_nyawa(screen, WIDTH - 100, 5, player.lives, player_mini_img)
    
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()