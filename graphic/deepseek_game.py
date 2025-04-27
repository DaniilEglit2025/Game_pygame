import pygame
import sys

#Инцилизация Pygame
pygame.init()

#Настройки окна
WIDTH, HEIGHT  = 800,600
FPS = 60

#Цвета
WHITE = (255, 255, 255)

#Инцилизация окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Animation")
clock = pygame.time.Clock()

#Класс для анимации
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.spritesheets = {
            'idle': self.load_spritesheet('Idle.png', 6),
            'walk': self.load_spritesheet('Walk.png', 8),
            'run': self.load_spritesheet('Run.png', 8),
        }
        self.current_animation = 'idle'
        self.sprites = self.spritesheets[self.current_animation]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprites]
        self.rect = self.image.get_rect(topleft=position)
        self.animation_speed = 0.2 #Скорость анимации
        self.last_update = pygame.time.get_ticks()
        self.facing_right = True  #Направление персонажа

        #Физика прыжка
        self.jump_speed = -15 #Начальная скорость прыжка
        self.gravity = 0.8 #Граваитация
        self.velocity_y = 0 #Текущая вертикальная скорость
        self.on_ground = True #Находится ли персонаж на земле
        self.jump_height = self.recrt.height #Высота прыжка (1.5x от роста)

        #Атака
        self.is_attacking = False #Флаг атаки
        self.attack_cooldown = 100 #Время перезарядки атаки (в мс)
        self.last_attack_time = 0 #Время последней атаки

        def load_spritesheet(self, filename, frames, flip=False):
            spritesheet= pygame.image.load(filename).convert_alpha()
            frame_width = spritesheet.get_width() // frames
            frame_height = spritesheet.get_height()
            sprites = []
            for i in range (frames):
                frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
                if flip: #Если нужно отразить спрайт
                    sprites.append(frame)
            return sprites

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > 100: #Обновление кадра каждые 100 мс
                self.last_update = now
                self.current_sprite += self.animation_speed
                if self.current_sprite >= len(self.sprites):
                    self.current_sprite = 0
                if self.is_attacking: #Если атака завершена
                    self.is_attacking = False
                    self.change_animation('idle') #Возвращаемся к idle после атаки
            self.image = self.sprites[int(self.current_sprite)]

            #Применяем гравитацию
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y

            #Ограничение на падение(земля)
            if self.rect.bottom >= HEIGHT:
                self.rect.bottom = HEIGHT
                self.velocity_y = 0
                self.on_ground = True

        def jump(self, direction):
            if self.on_ground: #Прыжок возможен только с земли
                self.velocity_y = self.jump_speed
                self.on_ground = False
                #выбор анимации прыжка в зависимости от направления
                if direction == 'right':
                    self.change_animation('jump_right')
                elif direction == 