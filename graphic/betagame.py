import pygame
import os
#Второй вариант отрисовки спрайтов, наследуемся от класса Sprite
SIZE = WEIGHT, HEIGHT = 600,400
BACKGROUND_COLOR = pygame.color('white')
FPS = 30

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Walk1'))
        self.images.append(pygame.image.load('Walk2'))
        self.images.append(pygame.image.load('Walk3'))
        self.images.append(pygame.image.load('Walk4'))
        self.images.append(pygame.image.load('Walk5'))
        self.images.append(pygame.image.load('Walk6'))
        self.index = 0
        self.image = self.images(self,index)
        self.rect = pygame.Rect(5, 5, 150, 198)

        def update(self):
            