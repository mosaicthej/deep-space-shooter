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
import random
import os,pygame,time
import classes_v2
import otherCodesThatsUseful as ocu

pygame.init()


BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
YELLOW = (255,255,0)
FREDRED = (230,58,36)

fps = 60
cycle = 0

sc_height = 800
sc_width = 550
screen = pygame.display.set_mode([sc_width,sc_height])

clock = pygame.time.Clock()
done = False

all_sprites_list = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
ply_bullets = pygame.sprite.Group()
enemy_list = []
heart,heart_empty = ocu.get_image('heart.png'),ocu.get_image('heart_empty.png')



x = 0
y = 0

width_player = 15
height_player = 15

Fred_test_image = pygame.image.load("Shrek_(N).png").convert()
Fred_test_image.set_colorkey(WHITE)

Bob = classes_v2.Player(GREEN, x, y)

bobo = classes_v2.Player(GREEN,x,y)

all_sprites_list.add(Bob)

#Fred = classes_v2.Enemy(Fred_test_image,RED,0,-300,178,269,1000,2.5,0,100)
#all_sprites_list.add(Fred)
#enemy_list.append(Fred)
def create_enemy():
    for i in range (10):
        health_amount = random.randint(20,100)
        length_health = health_amount/2
        goblin = classes_v2.Bird(0,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),random.randint(0,100),random.randint(-300,0),random.randint(20,80),random.randint(20,80),health_amount,(random.randint(1,10)/10),0,length_health,1,30)
        all_sprites_list.add(goblin)
        enemy_list.append(goblin)

Collins = classes_v2.Enemy(0,WHITE,-10,-60,570,50,10**2000,0,0,0,0,10)
all_sprites_list.add(Collins)
enemy_list.append(Collins)

bobo_list = pygame.sprite.Group()
bobo_list.add (bobo)

ply_health= 3
dmg_taken = 0
dmg_done = 0
kills = 10

picSerie = 0
picLyr = 18

immune,immune_blink = False,False
immune_frame = 0

pygame.mouse.set_visible(False)



while not done:





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

##    if not immune and immune_blink:
##        immune_blink = False
##    elif immune and not immune_blink:
##        immune_blink = True



    if immune:
        fps = 24
        if immune_blink:
            immune_blink = False
        else:
            immune_blink = True
    elif not immune:
        fps = 60
        immune_blink = False

    #Fred.image.fill ((230,58,36))

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


    plane00pic = ocu.get_image(picstr)          #animate the player

    if not immune_blink:
        bobo.image = plane00pic
    else:
        bobo.image.fill((0,0,0))

    screen.fill(BLACK)

    for i in range (0,ply_health-dmg_taken):  #heart
        screen.blit(heart, [10+20*(ply_health-1)*i,10])
    for i in range (0,dmg_taken):
        screen.blit(heart_empty,[10+20*(ply_health-1)*(ply_health-1-i),10])

    if kills ==10:
        create_enemy()
        kills = 0

    pos = pygame.mouse.get_pos()
    [x,y] = pos
    Bob.rect.x = x - width_player/2
    Bob.rect.y = y - height_player/2
    bobo.rect.x = Bob.rect.x-40
    bobo.rect.y = Bob.rect.y-50

    """if Bob.rect.y < (Fred.rect.y + Fred.height):
        Bob.rect.y = Fred.rect.y + Fred.height
        bobo.rect.y = Bob.rect.y - 50"""

##    for i in range (100):
    bullet_player = classes_v2.Bullet(ocu.randrgb(),(Bob.rect.x + width_player/2),bobo.rect.y,-20,[2,2])

    if not immune:
        ply_bullets.add(bullet_player)
        all_sprites_list.add(bullet_player)


    hit = pygame.sprite.spritecollide(Bob, enemy_bullets, True)

    for enemy in enemy_list:
        hit_enemy = pygame.sprite.spritecollide(enemy, ply_bullets, True)
        for bullet in hit_enemy:
            enemy.damage_taken += 1
        if enemy.max_health > enemy.damage_taken:
            enemy.update_enemy(cycle)
            enemy.draw_health(screen)
            enemy.shoot_enemy(cycle)
            for bullet in enemy.bullet_list:
                all_sprites_list.add(bullet)
                enemy_bullets.add(bullet)
        else:
            enemy.destroy()
            enemy_list.remove(enemy)
            kills += 1
            #Fred.image.fill ((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    #bullets_recycling = pygame.sprite.spritecollide(Collins,ply_bullets, True)

    #this is where we determine if the ship is hit
    for bullet in hit:
        print("hit")
        if not immune:
            dmg_taken += 1
        immune = True
    if immune:
        immune_frame+=1
        Bob.image.fill(WHITE)

        if immune_frame > fps*3:
            immune_frame = 0
            immune =False
            Bob.image.fill(GREEN)



    if dmg_taken == ply_health:
        done = True
    """if Fred.damage_taken == Fred.max_health:
        Fred.kill()
        Boss_dead = True"""
##        time.sleep(5)
        #done = True


    #changes the globins color as it moves, for artistic effect.
    for glb in enemy_list:
        glb.color = ( int(glb.rect.x/sc_width* 255),255-int(glb.rect.x/sc_width*255),random.randint(0,255) )


#    all_sprites_list.update()
    ply_bullets.update()
    enemy_bullets.update()
#       bobo.update()
    bobo_list.draw(screen)

    all_sprites_list.draw(screen)

    cycle+=1

    pygame.display.flip()
    clock.tick(fps)

##        rel = pygame.mouse.get_rel()
    print('collins',Collins.damage_taken)

pygame.quit()
