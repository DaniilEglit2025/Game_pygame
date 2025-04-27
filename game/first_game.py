import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
GREEN = (50, 205, 50)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


# Шрифты
hp_font = pygame.font.Font(None, 36)
font = pygame.font.Font(None, 36)

# Состояния игры
MENU = 0
GAME = 1

# Инициализация окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Animation with Jump and Attack")
clock = pygame.time.Clock()

# Загрузка фона
background = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

class Button:
    def __init__(self, text, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = ORANGE
        self.text_color = GREEN

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

class Bot(pygame.sprite.Sprite):
    def __init__(self, position, player):
        super().__init__()
        self.player = player
        self.hp = 100
        self.animation_speeds = {
            'idle':0.1,
            'walk_right':0.15,
            'walk_left':0.15,
            'attack_right':0.85,
            'attack_left':0.85
        }
        self.spritesheets = {
            'idle': self.load_spritesheet('assets/Shinobi/idle.png', 6),
            'walk_right': self.load_spritesheet('assets/Shinobi/walk.png', 8),
            'walk_left': self.load_spritesheet('assets/Shinobi/walk.png', 8, flip=True),
            'attack_right': self.load_spritesheet('asssets/Shinobi/attack.png', 5),
            'attack_left':self.load_spritesheet('assets/Shinobi/attack.png', 3, flip=True)
        }
        self.current_animation = 'idle'
        self.sprites = self.spritesheets(self.current_animation)
        self.current_sprite = 0
        self.image = self.sprites(self.current_sprite)
        self.rect = self.image.get_rect(topleft=position)
        self.animation_speed = self.animation_speeds(self.current_animation)
        self.last_update = pygame.time.get_ticks()
        self.gravity = 0.0
        self.velocity_y = 0
        self.on_ground = True
        self.is_attacking = False
        self.attack_cooldown = 1000
        self.last_attack_time = 0
        self.notice_distance = 4 * self.rect.width
        self.attack_distance = 2 * self.rect.height
        self.speed = 3

    def load_spritesheet(self, filename, frames, flip=False):
        spritesheet = pygame.image.load(filename).convert_alpha()
        frame_width = spritesheet.get_width() // frames
        frame_height = spritesheet.get_height()
        sprites = []
        for i in range(frames):
            frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            if flip:
                frame = pygame.transform.flip(frame, True, False)
            sprites.append(frame)
        return sprites

    def update(self):
        if self.hp <= 0:
            self.kill()
            global bot_respawn_time, bots_created
            if bots_created < 3:
                bot_respawn_time = pygame.time.get_ticks() + 1000
            return

        now = pygame.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.current_sprite = self.animation_speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                if self.is_attacking:
                    self.is_attacking = False
                    self.change_animation('idle')
            self.image = self.sprites[int(self.current_sprite)]
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity_y = 0
            self.on_ground = True
        distance_to_player = abs(self.rect.conterx - self.player.rect.centerx)
        if distance_to_player <= self.notice_distance:
            if distance_to_player <= self.attack_distance:
                self.attack()
            else:
                self.move_towards_player()
        else:
            if not self.is_attacking:
                self.change_animation()
    def move_towards_player(self):
        if self.player.recft.centerx > self.rect.centerx:
            self.rect.x += self.speed
            self.change_animation('walk_right')
        elif self.player.rect.centerx < self.rect.centerx:
            self.rect.x -= self.speed
            self.change_animation('walk left')

    def attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_attack_time > self.attack_cooldown:
            self.last_attack_time = now
            self.is_attaking = True
            if self.player.rect.centerx > self.rect.centerx:
                self.change_animation('attack_right')
            else:
                self.change_animation('attack_left')
            if abs(self.rect.centerx - self.player.rect.centerx) < self.attack_distance:
                self.player.hp -= 10

    def change_animation(self, animation):
        if self.current_animation != animation:


class AnimatedSprite(pygame.sprite.Sprite):
    # Класс персонажа остается без изменений из предыдущего кода
    def __init__(self, position):
        super().__init__()
        self.hp = 100

        self.animation_speeds = {
            'idle': 0.1,
            'walk_right': 0.15,
            'walk_left': 0.15,
            'jump_right': 0.75,
            'jump_left': 0.75,
            'attack_right': 0.85,
            'attack_left': 0.85
        }
        # Загружаем спрайты для анимаций
        self.spritesheets = {
            'idle': self.load_spritesheet('Idle.png', 6),
            'walk_right': self.load_spritesheet('Walk.png', 8),
            'walk_left': self.load_spritesheet('Walk.png', 8, flip=True),
            'jump_right': self.load_spritesheet('Jump.png', 12),
            'jump_left': self.load_spritesheet('Jump.png', 12, flip=True),
            'attack_right': self.load_spritesheet('player/Attack_1.png', 6),
            'attack_left': self.load_spritesheet('player/Attack_1.png', 6, flip=True),
        }
        self.current_animation = 'idle'
        self.sprites = self.spritesheets[self.current_animation]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(topleft=position)
        self.animation_speed = self.animation_speeds[self.current_animation]
        self.last_update = pygame.time.get_ticks()

        # Физика прыжка
        self.jump_speed = -15
        self.gravity = 0.8
        self.velocity_y = 0
        self.on_ground = True
        self.jump_height = self.rect.height * 1.5

        # Атака
        self.is_attacking = False
        self.attack_cooldown = 100
        self.last_attack_time = 0

    def load_spritesheet(self, filename, frames, flip=False):
        spritesheet = pygame.image.load(filename).convert_alpha()
        frame_width = spritesheet.get_width() // frames
        frame_height = spritesheet.get_height()
        sprites = []
        for i in range(frames):
            frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            if flip:
                frame = pygame.transform.flip(frame, True, False)
            sprites.append(frame)
        return sprites

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.current_sprite += self.animation_speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                if self.is_attacking:
                    self.is_attacking = False
                    self.change_animation('idle')
            self.image = self.sprites[int(self.current_sprite)]

        # Гравитация
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Столкновение с землей
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity_y = 0
            self.on_ground = True

    def jump(self, direction):
        if self.on_ground:
            self.velocity_y = self.jump_speed
            self.on_ground = False
            if direction == 'right':
                self.change_animation('jump_right')
            elif direction == 'left':
                self.change_animation('jump_left')

    def attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_attack_time > self.attack_cooldown:
            self.last_attack_time = now
            self.is_attacking = True
            if self.current_animation == 'walk_right' or self.current_animation == 'idle':
                self.change_animation('attack_right')
            elif self.current_animation == 'walk_left':
                self.change_animation('attack_left')

    def change_animation(self, animation):
        if self.current_animation != animation:
            self.current_animation = animation
            self.sprites = self.spritesheets[self.current_animation]
            self.current_sprite = 0
            self.animation_speed = self.animation_speeds[animation]

# Функция главного меню
def main_menu():
    play_button = Button("Играть", WIDTH//2 - 100, HEIGHT//2 - 60, 200, 50)
    exit_button = Button("Выйти", WIDTH//2 - 100, HEIGHT//2 + 10, 200, 50)
    
    while True:
        screen.fill(BLACK)
        play_button.draw(screen)
        exit_button.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(event.pos):
                    return GAME
                elif exit_button.rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if play_button.rect.collidepoint(event.pos):
                    play_button.color = (255, 140, 0)  # Более темный оттенок оранжевого
                else:
                    play_button.color = ORANGE
                if exit_button.rect.collidepoint(event.pos):
                    exit_button.color = (255, 140, 0)
                else:
                    exit_button.color = ORANGE

        clock.tick(FPS)

# Создание персонажаДа 
player = AnimatedSprite((100, HEIGHT - 150))
all_sprites = pygame.sprite.Group(player)

# Основной цикл игры
current_state = MENU
running = True

while running:
    if current_state == MENU:
        current_state = main_menu()
    
    elif current_state == GAME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player.current_animation in ['walk_right', 'idle']:
                        player.jump('right')
                    elif player.current_animation == 'walk_left':
                        player.jump('left')
                if event.key == pygame.K_a:
                    player.attack()

        # Управление персонажем
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if not player.is_attacking:
                player.change_animation('walk_right')
                player.rect.x += 5
        elif keys[pygame.K_LEFT]:
            if not player.is_attacking:
                player.change_animation('walk_left')
                player.rect.x -= 5
        else:
            if player.on_ground and not player.is_attacking:
                player.change_animation('idle')

        # Границы экрана
        if player.rect.left < 0:
            player.rect.left = 0
        if player.rect.right > WIDTH:
            player.rect.right = WIDTH

        # Отрисовка
        screen.blit(background, (0, 0))
        all_sprites.update()
        all_sprites.draw(screen)

        #Отрисовка здоровья
        hp_text = hp_font.render(f"HP: {player.hp}%", True, RED)
        screen.blit(hp_text, (WIDTH - 250, 10)) 

        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()
sys.exit()