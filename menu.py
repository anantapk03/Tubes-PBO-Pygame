import pygame
from window import *

font_name = pygame.font.match_font("arial")
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop  = (x, y)
    surf.blit(text_surface, text_rect)

class Menu():
    
    def show_go_screen():
        screen.blit(background, background_rect)
        draw_text(screen, "Shooters", 64, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, "Tekan kiri dan kanan untuk menghindar, S untuk nembak", 16, WIDTH / 2, HEIGHT / 2)
        draw_text(screen, "Tekan apa saja untuk mulai", 18, WIDTH / 2, HEIGHT * 3 / 4)
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    waiting = False
                    
    def show_gameover_screen(score):
        screen.blit(background, background_rect)
        draw_text(screen, "GAME OVER", 64, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, "Score anda {}".format(score), 45, WIDTH / 2, HEIGHT / 2)
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    waiting = False
