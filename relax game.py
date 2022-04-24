import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1400,700))
pygame.display.set_caption('Relaxing')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
start_time = 0
game_active = False

SQUARE_1 = pygame.Surface((50,50))
x = 0
y = 10
SQUARE_1.fill('Gold1')

SQUARE_2 = pygame.Surface((50,50))
x1 = 1350
y1 = 100
SQUARE_2.fill('Gold1')

SQUARE_3 = pygame.Surface((50,50))
x2 = 0
y2 = 200
SQUARE_3.fill('Gold1')

SQUARE_4 = pygame.Surface((50,50))
x3 = 1350
y3 = 300
SQUARE_4.fill('Gold1')

SQUARE_5 = pygame.Surface((50,50))
x4 = 0
y4 = 400
SQUARE_5.fill('Gold1')

SQUARE_6 = pygame.Surface((50,50))
x5 = 1350
y5 = 500
SQUARE_6.fill('Gold1')



SQUARE_7 = pygame.Surface((50,50))
x6 = 0
y6 = 600
SQUARE_7.fill('Gold1')

k = True
k1 = False
k2 = True
k3 = False
k4 = True
k5 = False
k6 = True

Menu = test_font.render('Relaxing game', False, (64, 64, 64))

text2 = test_font.render('Press the escape button to start', False, (64, 64, 64))

Statue = pygame.Surface((300,300))
Statue.fill('Gold1')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active == True:
        screen.fill((64,250,200))

        

        if k == True:
            x += 10
        if x == 1350:
            k = False

        if k == False:
            x -= 10

        if x == 0:
            k = True

        if k1 == True:
            x1 += 10
        if x1 == 1350:
            k1 = False

        if k1 == False:
            x1 -= 10

        if x1 == 0:
            k1 = True

        if k2 == True:
            x2 += 10
        if x2 == 1350:
            k2 = False

        if k2 == False:
            x2 -= 10

        if x2 == 0:
            k2 = True

        if k3 == True:
            x3 += 10
        if x3 == 1350:
            k3 = False

        if k3 == False:
            x3 -= 10

        if x3 == 0:
            k3 = True

        if k4 == True:
            x4 += 10
        if x4 == 1350:
            k4 = False

        if k4 == False:
            x4 -= 10

        if x4 == 0:
            k4 = True

        if k5 == True:
            x5 += 10
        if x5 == 1350:
            k5 = False

        if k5 == False:
            x5 -= 10

        if x5 == 0:
            k5 = True

        if k6 == True:
            x6 += 10
        if x6 == 1350:
            k6 = False

        if k6 == False:
            x6 -= 10

        if x6 == 0:
            k6 = True

        screen.blit(SQUARE_1, (x, y))
        screen.blit(SQUARE_2, (x1, y1))
        screen.blit(SQUARE_3, (x2, y2))
        screen.blit(SQUARE_4, (x3, y3))
        screen.blit(SQUARE_5, (x4, y4))
        screen.blit(SQUARE_6, (x5, y5))
        screen.blit(SQUARE_7, (x6, y6))

    else:

        screen.fill((64,250,200))
        screen.blit(Menu, (550, 100))
        screen.blit(text2, (430, 550))
        screen.blit(Statue, (525, 200))
        if event.type == pygame.KEYDOWN:
            game_active = True


    pygame.display.update()
    clock.tick(60)