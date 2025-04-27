import pygame


class Base_character(pygame.sprite.Sprite):
    
        def __init__(self, position, animation_config, animation_speeds):
            super().__init__()
            self.animation = ()
            self.animation_speeds = animation_speeds
            self.load_animations(animations_config)

            #Инциализация состояния анимации
            self.current_animation = 'idle'
            self.animation_frame = 0
            self.last_update = pygame.time.get_ticks

            #Основные свойства персонажа
            self.image = self.animations[self.current_animation]['frames'][0]
            self.rect = self.image.get_rect(tapleft=position)
            self.velocity = Vector2(0,0)
            self.facing_right = True
            self.on_ground = True
            self.is_attacking = False

            def load_animations(self, config):
                """Загрузка анимаций из конфига с использованием отдельных скоростей"""
                for anim_name, params in config.items():
                    frames = self.load_spritesheet(
                        params['path'],
                        params['frames'],
                        params.get['flip', False]
                    )

                    self.animation[anim_name] = {
                        'frames': frames,
                        'speed': self.animation_speeds.get(anim_name, 100)
                    }

def load_spritesheet(self, file_name, frames, flip=False):
    """Загрузка и разделение спрайтшита"""
    spritesheet.pygame.image