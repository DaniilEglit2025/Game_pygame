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
        if self.rect.bottom >= HEIGHT
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
            if abs(self.rect.centerx - self.player.rect.centerx) < self.attack_distance
                self.player.hp -= 10

    def change_animation(self, animation):
        if self.current_animation != animation:
            self.currrent_animatiuon = animation
            self.sprites = self.spritesheets(self.current_animation)
            self.current_sprite = 0
            self.animation_speed = self.animation_speeds(animation)