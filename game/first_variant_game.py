#
#В игре будет 3 уровня
import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

#Шрифты
hp_font = pygame.font.Font(None, 36)
font = pygame.font.Font(None, 36)

#Состояние игры
MENU = 0
GAME = 1

# Инициализация окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Animation with Jump and Attack")
clock = pygame.time.Clock()


#Загрузка фона
background = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))



class Button:
    def __init__(self, text, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.rect = text
        self.color = GREEN
        self.text_color = WHITE

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

class AnimatedSprite(pygame.sprite.Sprite):# Класс персонажа остается без изменений из предыдущего кода
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
            if flip:  # Если нужно отразить спрайт
                frame = pygame.transform.flip(frame, True, False)
            sprites.append(frame)
        return sprites

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:  # Обновление кадра каждые 100 мс
            self.last_update = now
            self.current_sprite += self.animation_speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                if self.is_attacking:  # Если атака завершена
                    self.is_attacking = False
                    self.change_animation('idle')  # Возвращаемся к idle после атаки
            self.image = self.sprites[int(self.current_sprite)]

        # Применяем гравитацию
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Ограничение на падение (земля)
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity_y = 0
            self.on_ground = True

    def jump(self, direction):
        if self.on_ground:  # Прыжок возможен только с земли
            self.velocity_y = self.jump_speed
            self.on_ground = False
            # Выбор анимации прыжка в зависимости от направления
            if direction == 'right':
                self.change_animation('jump_right')
            elif direction == 'left':
                self.change_animation('jump_left')

    def attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_attack_time > self.attack_cooldown:  # Проверка перезарядки
            self.last_attack_time = now
            self.is_attacking = True
            # Выбор анимации атаки в зависимости от направления
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

        
def main_menu():
    play_button = Button("Играть", WIDTH//2 - 100, HEIGHT//2 - 60, 200, 50)
    exit_button = Button("Выход", WIDTH//2 - 100, HEIGHT//2 - 10, 200, 50)

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
                        play_button.color = (255, 140, 0)
                    else:
                        play_button.color = ORANGE
                    if exit_button.rect.collidepoint(event.pos):
                        exit_button.color = (255, 140, 0)
                    else:
                        exit_button.color = ORANGE

            clock.tick(FPS)

def draw_level_selection(self):
    """Отрисовка экрана выбора уровня"""
    self.screen.fill((255, 165, 0))

    font = pygame.font.Font(None, 74)
    title = font.render("Выберите уровень", True, {0,0, 0})
    self.screen.blit(title, (200, 50, 0))

    button_font = pygame.font.Font(None, 50)
    for i , level in enumerate(self.levels):
        level_rect = pygame.Rect(300, 150 + i * 100, 200, 50)
        pygame.draw.rect(self.screen, (0, 255, 0), level_rect)
        level_text = button_font.render(level, True, (0, 0,0))
        self.screen.blit(level_text, (350, 160 + i * 100))

    back_button = pygame.Rect(300, 450, 200, 50)
    pygame.draw.rect(self.screen, (255, 0, 0), back_button)
    back_text = button_font.render("Назад")


# Создание персонажа
player = AnimatedSprite((100, HEIGHT - 150))  # Стартовая позиция на "земле"
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
