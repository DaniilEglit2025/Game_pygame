import pygame
import random

pygame.init()
WIDTH = 500
HEIGHT = 600
size = (WIDTH, HEIGHT)
win = pygame.display.set_mode(size)
clock = pygame.time.Clock()

score = 0
font = pygame.font.SysFont('Verdana', 30)

pygame.mixer.music.load('banban 3.mp3')
pygame.mixer.music.play(-1)

sound_bang = pygame.mixer.Sound('выстрел.mp3')

hero = pygame.image.load('1234.png')
hero = pygame.transform.smoothscale(hero, (100, 100))
hero_rect = hero.get_rect()

rocket = pygame.image.load('5678.png')
rocket = pygame.transform.smoothscale(rocket, (110, 95))
rocket_rect = rocket.get_rect()

smile = pygame.image.load('Diablo-PNG-Photos.png')
smile = pygame.transform.smoothscale(smile, (80, 70))
smile_rect = smile.get_rect()

print(hero_rect)

isRunning = True
isShot = False
isShotting = False
x = 100
y = 100
r = 30
ax = []
ay = []
rocket_rects = []
smile_rect.x = random.randint(0, WIDTH - smile_rect.width)
smile_rect.y = 0
while isRunning:
    #обработка событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            isRunning = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            isShot = True

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_RIGHT]:
        x += 10
        if x>WIDTH-hero_rect.width:
            x -= 10
    if key_pressed[pygame.K_LEFT]:
        x -= 10
        if x < 0:
            x += 10
    if key_pressed[pygame.K_UP]:
        y -= 10
        if y < r:
            y += 10
    if key_pressed[pygame.K_DOWN]:
        y += 10
        if y > HEIGHT - hero_rect.height:
            y -= 10

    hero_rect.x = x
    hero_rect.y = y
    #расчёт новых координат
    if isShot == True:
        r_x = x + hero_rect.width//2 - rocket_rect.width//2
        r_y = y
        r = pygame.Rect(r_x, r_y, rocket_rect.width, rocket_rect.height)
        rocket_rects.append(r)
        #ax.append(r_x)
        #ay.append(r_y)
        isShot = False
        isShotting = True
    if isShotting == True:
        for i in range(len(rocket_rects)):
            rocket_rects[i].y -= 8

    #полёт демона
    smile_rect.y += 5
    if smile_rect.y > HEIGHT:
        smile_rect.y = 0
        smile_rect.x = random.randint(0, WIDTH - smile_rect.width)

    #проверка столкновений
    for r in rocket_rects:
        if r.colliderect(smile_rect):
            rocket_rects.remove(r)
            smile_rect.x = random.randint(0, WIDTH - smile_rect.width)
            smile_rect.y = 0
            score += 1
            sound_bang.play()
    if hero_rect.colliderect(smile_rect):
        #isRunning = False
        pygame.mixer.music.stop()
        pygame.mixer.Sound('аааааа.mp3').play()

    f = font.render('Очки' + str(score), True, (250,250,90))

    #рисование персонажей
    win.fill( (0,0,0) )
    #pygame.draw.circle(win,(255,0,0), (x,y), r) #
    win.blit(hero, (x,y))
    if isShotting == True:
        for i in range(len(rocket_rects)):
            win.blit(rocket, rocket_rects[i])
    win.blit(smile, smile_rect)
    win.blit(f, (0,0))
    #обновить экран
    pygame.display.update()
    #контроль FPS
    clock.tick(60)