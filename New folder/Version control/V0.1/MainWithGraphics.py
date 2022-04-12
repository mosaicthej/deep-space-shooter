#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      4601465
#
# Created:     11/05/2018
# Copyright:   (c) 4601465 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
import random,os
import pygame
import classes
import time

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
            _image_library[path] = image
    return image


pygame.init()

BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
YELLOW = (255,255,0)

height = 800
width = 550
screen = pygame.display.set_mode([width,height])

clock = pygame.time.Clock()
done = False

all_sprites_list = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
bullets = pygame.sprite.Group()
heart = pygame.image.load("heart.png").convert()

x = 0
y = 0

width_player = 15
height_player = 15

Bob = classes.Player(GREEN, x, y)
Bob = classes.Player(GREEN, x, y)

bobo = classes.Player(GREEN,x,y)

all_sprites_list.add(Bob)

Fred = classes.Enemy(RED, x, y ,200,100)
all_sprites_list.add(Fred)

bobo_list = pygame.sprite.Group()
bobo_list.add (bobo)


dmg_taken = 0
dmg_done = 0

cycle = 0

picSerie = 0
picLyr = 18

Boss_dead = False

while not done:

    Fred.image.fill ((230,58,36))

    picSerie += 1
    picLyr -= 1
    if picSerie >17:
        picSerie = 0
    if picLyr < 1:
        picLyr = 18
    if picSerie<10:
        picstr = 'plane02_000'+str(picSerie)+'_Layer-'+str(picLyr)+'.png'
    elif picSerie >=10:
        picstr = 'plane02_00'+str(picSerie)+'_Layer-'+str(picLyr)+'.png'

    plane00pic = get_image(picstr)
    bobo.image = plane00pic


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    for i in range (0,3-dmg_taken):
        heart.set_colorkey(WHITE)
        screen.blit(heart, [10+50*i,10])

    pos = pygame.mouse.get_pos()
    [x,y] = pos
    Bob.rect.x = x - width_player/2
    Bob.rect.y = y - height_player/2
    bobo.rect.x = Bob.rect.x-40
    bobo.rect.y = Bob.rect.y-50

    Fred.rect.y = 50
    if cycle % (2*(width - Fred.width)) == cycle % (width - Fred.width):
        Fred.rect.x = 0 + cycle % (width - Fred.width)
    else:
        Fred.rect.x = (width - Fred.width) - cycle % (width - Fred.width)

    if Bob.rect.y < (Fred.rect.y + Fred.height):
        Bob.rect.y = Fred.rect.y + Fred.height
        bobo.rect.y = Bob.rect.y - 50

    if Boss_dead == False:
        if cycle % 15 == 0:
            for i in range (5):
                bullet_boss = classes.Bullet(YELLOW,(Fred.rect.x + i/4*Fred.width),(Fred.rect.y + Fred.height),random.randint(3,8))
                all_sprites_list.add(bullet_boss)
                enemy_bullets.add(bullet_boss)

    for i in range (1):
        bullet_player = classes.Bullet(WHITE,(Bob.rect.x + width_player/2),Bob.rect.y,-20,[2,2])

        bullets.add(bullet_player)
        all_sprites_list.add(bullet_player)

    hit = pygame.sprite.spritecollide(Bob, enemy_bullets, True)
    if Boss_dead == False:
        hit_enemy = pygame.sprite.spritecollide(Fred, bullets, True)
    else:
        hit_enemy = ()
    for bullet in hit:
        print("hit")
        dmg_taken += 1

    for bullet in hit_enemy:
        print(1000 - dmg_done)
        dmg_done += 1
        Fred.image.fill ((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    if dmg_taken == 3:
        done = True
    if dmg_done == 1000:
        Fred.kill()
        Boss_dead = True
        time.sleep(5)
        done = True

    all_sprites_list.update()
    bobo.update()
    bobo_list.draw(screen)

    all_sprites_list.draw(screen)

    pygame.draw.rect(screen, WHITE,[400,9,102,13],0)

    for i in range (0,math.floor((1000-dmg_done)/10),1):
        Health = (255 - i*255/99,i*255/99,0)
        pygame.draw.line(screen,Health,[401+i,10],[401+i,20])

    cycle+=1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()