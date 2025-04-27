import sys
import pyganim
import pygame
from pygame.locals import *


pygame.init()
windowSurFace = pygame.display.set_mode((320, 240), 0, 32)
images = pyganim.getImagesFromSpriteSheet("Walk.png", rows=1, cols=8, rects=[])
frames = list(zip(images, [200, 200, 600]))
animObj = pyganim.PygAnimation(frames)
animObj.play()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock = pygame.time.Clock()

    windowSurFace.fill((100, 50, 50))
    animObj.blit(windowSurFace, (100, 100))
    pygame.display.update


