import pygame
from player import Player
from window import *
from meteor import Meteor
from menu import *

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

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()