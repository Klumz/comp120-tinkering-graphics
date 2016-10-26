import pygame, sys, time
from pygame.locals import *
pygame.init()

Black = (0, 0, 0)
White = (255, 255, 255)

Height = 1448
Width = 880

Display = pygame.display.set_mode((Height, Width), 0, 32)

pygame.display.set_caption("Meme name WIP")

# Meme text font, size, anti-aliasing and colour
Textfont = pygame.font.SysFont("impact", 100)
Fontimg = Textfont.render("test", 1, White)
Textfont2 = pygame.font.SysFont("impact", 100)
Fontimg2 = Textfont2.render("test", 1, White)

# Loads, draws and updates the meme/display
Meme = pygame.image.load("swords.jpg")
Display.blit(Meme, (0, 0))
Display.blit(Fontimg, (880/2, 0))
Display.blit(Fontimg2, (880/2, 1448/2))
pygame.display.update()


while True:

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            elif event.type == KEYDOWN:
             if event.key == K_ESCAPE:
                 sys.exit()
