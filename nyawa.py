import pygame

class Nyawa:
    
    def gambar_nyawa(surf, x, y, lives, img):
        for i in range(lives):
            img_rect = img.get_rect()
            img_rect.x = x + 30 * i
            img_rect.y = y
            surf.blit(img, img_rect)