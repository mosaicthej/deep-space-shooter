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
import os,pygame,time,datetime
import classes_vX3
import otherCodesThatsUseful as ocu
import PIL



def main():
    print('initializing Pygame....(0/1)')
    pygame.init()
    pygame.display.set_caption('Deep Space Shooter, a bullet hell game')
    print('1/1')

##    print('sound fx loading...(0/2)')
##    sfx_laser_str,sfx_spcTrs_str,sfx_zap_str = ['sfx-laser1.ogg','sfx-laser2.ogg','sfx-laser3.ogg','sfx-laser4.ogg','sfx-laser5.ogg'],['sfx-spaceTrash1.ogg','sfx-spaceTrash2.ogg'],['sfx-zap01.ogg','sfx-zap02.ogg','sfx-zap03.ogg']
##    sfx_pkg_str = [sfx_laser_str,sfx_spcTrs_str,sfx_zap_str]
##    print('(1/2)')
##
##    sfx_pkg = []
##    for l0 in sfx_pkg_str:
##        for l1 in l0:
##            s = pygame.mixer.Sound(l1)
##            sfx_pkg.append(s)
##    print('(2/2)')


    print('bgm loading...')
    bgm_lst_str = ['bgm001.ogg','bgm002.ogg','bgm003.ogg','Shanghai Alice of Meiji 17_1.ogg',
                    'Shanghai Alice of Meiji 17_2.ogg',
                    'Lunatic Princess!.ogg','Border of Life!.ogg','Eastern Dream.ogg',
                    'Flowering Night_2.ogg','Heian Alien.ogg',
                    'Wind God Girl!.ogg','Youkai Lost.ogg','giligiliEye.ogg.ogg','gokuraku jodo.ogg']
    pygame.mixer.music.load(random.choice(bgm_lst_str))
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    print('bgm ready!!')


##    background_image = pygame.image.load("space_background_test.jpg")
##
##    bg_pic00 = ocu.get_image('background00.png')
##
##    bg_lst = []
##
##    for i in range (10,360,30):
##        print('loading graphics--background', str(i/360*100),'%')
##        new_bg = ocu.hueShift('background00.png',i)
##        bg_lst.append(new_bg)
##    print('graphic background initalized!!')

    #bg_h = PIL.Image.

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
    #heart, heart_empty = pygame.image.load("heart.png").convert, pygame.image.load("heart_empty.png").convert

    blue1, blue2, blue3, blue4 =  ocu.get_image('blue_shitstarship1-pixilart.png'),ocu.get_image('blue_shitstarship2-pixilart.png'),ocu.get_image('blue_shitstarship3-pixilart.png'),ocu.get_image('blue_shitstarship4-pixilart.png')
    green1, green2, green3, green4 =  ocu.get_image('green_shitstarship1-pixilart.png'),ocu.get_image('green_shitstarship2-pixilart.png'),ocu.get_image('green_shitstarship3-pixilart.png'),ocu.get_image('green_shitstarship4-pixilart.png')
    red1, red2, red3, red4 =  ocu.get_image('red_shitstarship1-pixilart.png'),ocu.get_image('red_shitstarship2-pixilart.png'),ocu.get_image('red_shitstarship3-pixilart.png'),ocu.get_image('red_shitstarship4-pixilart.png')

    x = 0
    y = 0

    width_player = 15
    height_player = 15

    Bob = classes_vX3.Player(GREEN, x, y)

    bobo = classes_vX3.Player(GREEN,x,y)

    all_sprites_list.add(Bob)

    wave = 0
    ply_power = 10
    score=0
    power_up_frame = 0



    bgPic_lst = []
    bg_pic_h = PIL.Image.open('background.png_0030_Hue_Saturation-1-copy-6.png').size[1]
    print(bg_pic_h)
    for bgSerie in range(36):
        print('initializating background ('+str(bgSerie+1)+'/36)', '  ', int((bgSerie+1)/36*100),'%')

        bgLyr = 36-bgSerie
        if bgSerie < 10:
            bgStr = 'background.png_000'+str(bgSerie)+'_Hue_Saturation-1-copy-'+str(bgLyr)+'.png'
        elif bgSerie >10:
            bgStr = 'background.png_00'+str(bgSerie)+'_Hue_Saturation-1-copy-'+str(bgLyr)+'.png'

        bgPic_lst.append(ocu.get_image(bgStr))
    bgPic_pos=[]
    for i in range(len(bgPic_lst)) :
        bgPic_pos.append([0,bg_pic_h*i])

    bullet_str_lst = ['bullet_0000_Hue_Saturation-1-copy-5.png','bullet_0001_Hue_Saturation-1-copy-4.png','bullet_0002_Hue_Saturation-1-copy-3.png','bullet_0003_Hue_Saturation-1-copy-2.png','bullet_0004_Hue_Saturation-1-copy.png']
    bullet_img_lst = []

    print('loading bullets......')
    for st in bullet_str_lst:
        bullet_img_lst.append(ocu.get_image(st))

    warning_img_lst =[]
    for i in range (0,11):
        warning_img_lst.append(ocu.get_image('warning'+str(i)+'.png'))
    warn_serie = 0

    trump_img_lst = []
    for i in range(1,31):
        if i <11:
            trump_img_lst.append(ocu.get_image('trumpMLayer-'+str(31-i)+'.png'))
        else:
            trump_img_lst.append(ocu.get_image('trumpM_00'+str(i)+'_Layer-'+str(31-i)+'.png'))
        print('loading Trump (',i,'/31),',int(i/30*100),'%')

    trump_serie = 0
    boss00 = trump_img_lst[trump_serie]









    #Fred = classes_vX3.Enemy(Fred_test_image,RED,0,-300,178,269,1000,2.5,0,100)
    #all_sprites_list.add(Fred)
    #enemy_list.append(Fred)
##    def create_enemy():
##        for i in range (10):
##            wave_modifier = (1.1)**(wave-1)
##            health_variable = random.randint(20,100)
##            health_amount = health_variable*wave_modifier
##            length_health = health_variable/2
##
##            if wave % 4 == 1:
##                goblin = classes_vX3.Bird(0,((health_variable-20)*5/8,250-(health_variable-20)*15/8,(health_variable-20)*5/8),random.randint(0,100),random.randint(-300,0),health_variable,health_variable,health_amount,5-(health_variable-19)/16,0,length_health,1,30)
##                if goblin.change_y < 1:
##                    goblin.change_y = 1
##                all_sprites_list.add(goblin)
##                enemy_list.append(goblin)
##
##            if wave % 4 == 2:
##                ghost = classes_vX3.Ghost(0,(250-(health_variable-20)*15/8,(health_variable-20)*5/8,(health_variable-20)*5/8),random.randint(0,100),random.randint(-300,0),health_variable,health_variable,health_amount,5-(health_variable-19)/16,0,length_health,1,60)
##                all_sprites_list.add(ghost)
##                enemy_list.append(ghost)
##
##            if wave % 4 == 3:
##                piggy = classes_vX3.Hog(0,((health_variable-20)*5/8,(health_variable-20)*5/8,250-(health_variable-20)*15/8),random.randint(0,100),random.randint(-300,0),health_variable,health_variable,health_amount,5-(health_variable-19)/16,0,length_health,1,50)
##                if piggy.change_y < 1:
##                    piggy.change_y = 1
##                all_sprites_list.add(piggy)
##                enemy_list.append(piggy)
##
##        if wave % 4 == 0:
##
##            for i in range (3):
##                wave_modifier = (1.1)**(wave-1)
##                health_variable = random.randint(20,100)
##                health_amount = health_variable*wave_modifier
##                length_health = health_variable/2
##                goblin = classes_vX3.Bird(0,((health_variable-20)*5/8,250-(health_variable-20)*15/8,(health_variable-20)*5/8),random.randint(0,100),random.randint(-300,0),health_variable,health_variable,health_amount,5-(health_variable-19)/16,0,length_health,1,30)
##                if goblin.change_y < 1:
##                    goblin.change_y = 1
##                all_sprites_list.add(goblin)
##                enemy_list.append(goblin)
##
##            for i in range (4):
##                wave_modifier = (1.1)**(wave-1)
##                health_variable = random.randint(20,100)
##                health_amount = health_variable*wave_modifier
##                length_health = health_variable/2
##                ghost = classes_vX3.Ghost(0,(250-(health_variable-20)*15/8,(health_variable-20)*5/8,(health_variable-20)*5/8),random.randint(0,100),random.randint(-300,0),health_variable,health_variable,health_amount,5-(health_variable-19)/16,0,length_health,1,60)
##                all_sprites_list.add(ghost)
##                enemy_list.append(ghost)
##
##            for i in range (3):
##                wave_modifier = (1.1)**(wave-1)
##                health_variable = random.randint(20,100)
##                health_amount = health_variable*wave_modifier
##                length_health = health_variable/2
##                piggy = classes_vX3.Hog(0,((health_variable-20)*5/8,(health_variable-20)*5/8,250-(health_variable-20)*15/8),random.randint(0,100),random.randint(-300,0),health_variable,health_variable,health_amount,5-(health_variable-19)/16,0,length_health,1,50)
##                if piggy.change_y < 1:
##                    piggy.change_y = 1
##                all_sprites_list.add(piggy)
##                enemy_list.append(piggy)



    #(random.randint(0,255),random.randint(0,255),random.randint(0,255))

    for c in enemy_list:
        c.color = ((health_variable/health_amount)*255,(health_variable/health_amount)*255,(health_variable/health_amount)*255)
        print(c,c.color)

    Collins = classes_vX3.Enemy(0,WHITE,-10,-60,570,50,10**2000,0,0,0,0,10)
    all_sprites_list.add(Collins)
    enemy_list.append(Collins)

    bobo_list = pygame.sprite.Group()
    bobo_list.add (bobo)

    ply_health= 3
##    if  wave%5== 1 and ply_health<5:
##        ply_health +=1
##    if ply_power <12 and wave%3 == 1:
##        ply_power += random.choice([1,1,1,1,1,2,2,2,3,3])
    dmg_taken = 0
    dmg_done = 0
    kills = 10
    scr_multi = 1

    picSerie = 0
    picLyr = 18
##    bgSerie = 0
##    bgLyr = 36

    immune,immune_blink = False,False
    immune_frame = 0

    pygame.mouse.set_visible(False)

    wait = 0
    font = pygame.font.SysFont("Comic Sans",25,True,False)

    frm_sur = 0

    fps_now,last_fps = 0,0

    def create_enemy():
        global score,scr_multi

        wave_modifier = (1.15)**(wave-1)
        for i in range (10):

            health_variable = random.randint(20,100)
            health_amount = health_variable*wave_modifier
            length_health = health_variable/2

            if wave % 5 == 1:
                if 20<=health_variable<=40:
                    size = 40
                    image = green1
                if 40<health_variable<=60:
                    size = 60
                    image = green2
                if 60<health_variable<=80:
                    size = 80
                    image = green3
                if 80<health_variable<=100:
                    size = 100
                    image = green4
                goblin = classes_vX3.Bird(image,(0,0,0),random.randint(0,100),random.randint(-300,0),size,size,health_amount,5-(health_variable-19)/16,0,length_health,1,30)
                if goblin.change_y < 1:
                    goblin.change_y = 1
                all_sprites_list.add(goblin)
                enemy_list.append(goblin)


            if wave % 5 == 2:
                    if 20<=health_variable<=40:
                        size = 40
                        image = red1
                    if 40<health_variable<=60:
                        size = 60
                        image = red2
                    if 60<health_variable<=80:
                        size = 80
                        image = red3
                    if 80<health_variable<=100:
                        size = 100
                        image = red4
                    ghost = classes_vX3.Ghost(image,(0,0,0),random.randint(0,100),random.randint(-300,0),size,size,health_amount,5-(health_variable-19)/16,0,length_health,1,60)
                    all_sprites_list.add(ghost)
                    enemy_list.append(ghost)


            if wave % 5 == 3:
                if 20<=health_variable<=40:
                    size = 40
                    image = blue1
                if 40<health_variable<=60:
                    size = 60
                    image = blue2
                if 60<health_variable<=80:
                    size = 80
                    image = blue3
                if 80<health_variable<=100:
                    size = 100
                    image = blue4
                piggy = classes_vX3.Hog(image,(0,0,0),random.randint(0,100),random.randint(-300,0),size,size,health_amount,5-(health_variable-19)/16,0,length_health,1,50)
                if piggy.change_y < 1:
                    piggy.change_y = 1
                all_sprites_list.add(piggy)
                enemy_list.append(piggy)



        if wave % 5 == 4:

            for i in range (3):

                health_variable = random.randint(20,100)
                health_amount = health_variable*wave_modifier
                length_health = health_variable/2
                if 20<=health_variable<=40:
                    size = 40
                    image = green1
                if 40<health_variable<=60:
                    size = 60
                    image = green2
                if 60<health_variable<=80:
                    size = 80
                    image = green3
                if 80<health_variable<=100:
                    size = 100
                    image = green4
                goblin = classes_vX3.Bird(image,(0,0,0),random.randint(0,100),random.randint(-300,0),size,size,health_amount,5-(health_variable-19)/16,0,length_health,1,30)
                if goblin.change_y < 1:
                    goblin.change_y = 1
                all_sprites_list.add(goblin)
                enemy_list.append(goblin)

            for i in range (4):
                #wave_modifier = (1.1)**(wave-1)
                health_variable = random.randint(20,100)
                health_amount = health_variable*wave_modifier
                length_health = health_variable/2
                if 20<=health_variable<=40:
                    size = 40
                    image = red1
                if 40<health_variable<=60:
                    size = 60
                    image = red2
                if 60<health_variable<=80:
                    size = 80
                    image = red3
                if 80<health_variable<=100:
                    size = 100
                    image = red4
                ghost = classes_vX3.Ghost(image,(0,0,0),random.randint(0,100),random.randint(-300,0),size,size,health_amount,5-(health_variable-19)/16,0,length_health,1,60)
                all_sprites_list.add(ghost)
                enemy_list.append(ghost)

            for i in range (3):

                health_variable = random.randint(20,100)
                health_amount = health_variable*wave_modifier
                length_health = health_variable/2
                if 20<=health_variable<=40:
                    size = 40
                    image = blue1
                if 40<health_variable<=60:
                    size = 60
                    image = blue2
                if 60<health_variable<=80:
                    size = 80
                    image = blue3
                if 80<health_variable<=100:
                    size = 100
                    image = blue4
                piggy = classes_vX3.Hog(image,(0,0,0),random.randint(0,100),random.randint(-300,0),size,size,health_amount,5-(health_variable-19)/16,0,length_health,1,50)
                if piggy.change_y < 1:
                    piggy.change_y = 1
                all_sprites_list.add(piggy)
                enemy_list.append(piggy)

        if wave % 5 == 0:
            #wave_modifier = (1.1)**(wave-1)
            health_variable = 1000
            health_amount = health_variable*wave_modifier
            length_health = health_variable/4
            image = trump_img_lst[trump_serie]
            Boss_man = classes_vX3.Boss(image,(234,130,150),0,0,300,200,health_amount,1,0,length_health,50,10)
            all_sprites_list.add(Boss_man)
            enemy_list.append(Boss_man)



#-------------------------main game loop----------------------------------------##
#-------------------------------------------------------------------------------##
#-------------------------------------------------------------------------------##

    import time #timer
    t0 = time.clock()
    print("ready to go, good luck!")


    while not done:

        frm_sur += 1
        if frm_sur ==15:
            score += 1 * scr_multi/10
            frm_sur =0
        wave_modifier = (1.15)**(wave-1)
        power_up_boo = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load(random.choice(bgm_lst_str))
                pygame.mixer.music.play()

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

        picSerie += 1
        picLyr -= 1

        bgSerie +=1
        bgLyr -=1


        if picSerie >17:
            picSerie = 0
        if picLyr < 1:
            picLyr = 18
        if picSerie<10:
            picstr = 'plane02_000'+str(picSerie)+'_Layer-'+str(picLyr)+'.png'
        elif picSerie >=10:
            picstr = 'plane02_00'+str(picSerie)+'_Layer-'+str(picLyr)+'.png'




        plane00pic = ocu.get_image(picstr)          #animate the player
##        bgPic = ocu.get_image(bgStr)

        #Fred.image.fill ((230,58,36))
        screen.fill(BLACK)
##        for pic in bgPic_lst:
##            screen.blit(pic,bgPic_pos[bgPic_lst.index(pic)])

        for i in range (len(bgPic_lst)):
            screen.blit(bgPic_lst[i],bgPic_pos[i])
            if bgPic_pos[i][1] < -1*bg_pic_h:
                bgPic_pos[i][1] = len(bgPic_lst)*bg_pic_h

        for pos in bgPic_pos:
            pos[1]-=1


##        screen.blit(bgPic,[0,0])

##        screen.blit(background_image,[0,(cycle % 171) - 171])
##        screen.blit(background_image,[0,cycle % 171])
##        screen.blit(background_image,[0,(cycle % 171) + 171])
##        screen.blit(background_image,[0,(cycle % 171) + 342])
##        screen.blit(background_image,[0,(cycle % 171) + 513])
##        screen.blit(background_image,[0,(cycle % 171) + 684])
##        screen.blit(background_image,[295,(cycle % 171) - 171])
##        screen.blit(background_image,[295,cycle % 171])
##        screen.blit(background_image,[295,(cycle % 171) + 171])
##        screen.blit(background_image,[295,(cycle % 171) + 342])
##        screen.blit(background_image,[295,(cycle % 171) + 513])
##        screen.blit(background_image,[295,(cycle % 171) + 684])




        if not immune_blink:
            bobo.image = plane00pic
        else:
            bobo.image = pygame.Surface([1,1])

        for i in range (0,ply_health-dmg_taken):  #heart
            screen.blit(heart, [10+20*(ply_health-1)*i,10])
        for i in range (0,dmg_taken):
            screen.blit(heart_empty,[10+20*(ply_health-1)*(ply_health-1-i),10])


        if kills ==10:
            wait = cycle
            kills = 0

        if wave%5 ==4:

            if cycle in range  (wait+120, wait+540):
                screen.blit(warning_img_lst[warn_serie],[0,300])
                warn_serie += 1
                if warn_serie == 11:
                    warn_serie = 0

            if cycle == wait +540:

                wait = 0
                wave+=1
                create_enemy()

        elif wave %5 ==0 and wave>1:
                trump_serie += 1
                if trump_serie == 30:
                    trump_serie = 1
                enemy_list[len(enemy_list)-1].image = trump_img_lst[trump_serie]
                if cycle == wait +300:
                    wait = 0
                    wave +=1
                    create_enemy()






        else:
            if cycle == wait+300:
                wait = 0
                wave+=1
                if  wave%3== 1 and wave > 1 and dmg_taken>0:
                    dmg_taken-=1
                if ply_power <12 and wave%5 == 1 and wave > 1:
                    power_up_boo = True
                    power_up_val =random.choice([1])
                    ply_power +=  power_up_val
                    power_up_frame = 1
                create_enemy()




        pos = pygame.mouse.get_pos()
        [x,y] = pos
        Bob.rect.x = x - width_player/2
        Bob.rect.y = y - height_player/2
        bobo.rect.x = Bob.rect.x-40
        bobo.rect.y = Bob.rect.y-50

        scr_multi = ((sc_height-y)*3)/sc_height
        scr_multi = scr_multi+1
        scr_multi = int(scr_multi*1000)
        scr_multi = scr_multi/1000
        if not wave <2:
            scr_multi = ((math.log(wave_modifier))/math.log(1.12))*scr_multi

        """add a "score multiplier" variable,
           the closer the player gets to the top,
           the higher his multiplier will be, varies from
           1 to 11 (100.0% to 1100.0%)
           then multiply by the log_base 1.12 of the wave modifier """

        """ Score spec: the player's basic score going up by 1 for every 15 frames (approx. 0.25 second) he survived, up by 10 for each bullet hit the enemy,
        30 for globlin, 70 for ghost, 100 for hogs and 80 when wave%4 == 0, 300 for each boss, then multiply the score_multi
        the surviving score will only account for one tenth of the score_multiplier """


    ##    for i in range (100):
    # I have overwrote the code for muti-layer bullets for player here, you can change it by change the variable 'ply_power'
    ##    bullet_player = classes_vX3.Bullet(ocu.randrgb(),(Bob.rect.x + width_player/2),bobo.rect.y,0,-10,[2,2])
    ##
    ##    if not immune:
    ##        ply_bullets.add(bullet_player)
    ##        all_sprites_list.add(bullet_player)
        for i in range (1,ply_power):
            if not immune:
                ply_bullets.add(classes_vX3.Bullet(ocu.randrgb(),(Bob.rect.x+3 + width_player/2),bobo.rect.y,random.randint(-1*i+1,i-1),-15,[2,2]))
                all_sprites_list.add(classes_vX3.Bullet(ocu.randrgb(),(Bob.rect.x+3 + width_player/2),bobo.rect.y,random.randint(-1*i+1,i-1),-15,[2,2]))

        hit = pygame.sprite.spritecollide(Bob, enemy_bullets, True)

        for enemy in enemy_list:
            hit_enemy = pygame.sprite.spritecollide(enemy, ply_bullets, True)
            for bullet in hit_enemy:
                enemy.damage_taken += 1
                scr_hit = 20
                score += scr_hit*scr_multi
            if enemy.max_health > enemy.damage_taken:
                enemy.update_enemy(cycle)
                enemy.draw_health(screen)
                enemy.shoot_enemy(cycle,Bob.rect.x,Bob.rect.y)
                for bullet in enemy.bullet_list:
                    bullet.update()
                    all_sprites_list.add(bullet)
                    enemy_bullets.add(bullet)
            else:
                enemy.destroy()
                if wave %1 == 0:
                    scr_kill = 30
                    score +=scr_kill*scr_multi
                elif wave %2 == 0:
                    scr_kill = 70
                    score +=scr_kill*scr_multi
                elif wave %3 == 0:
                    scr_kill = 100
                    score +=scr_kill*scr_multi
                elif wave %4 == 0:
                    scr_kill = 80
                    score +=scr_kill*scr_multi
                elif wave%5 == 0:
                    scr_kill = 300
                    score += scr_kill


                enemy_list.remove(enemy)
                if wave%5 == 0:
                    kills += 10

                else:
                    kills += 1

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
        all_sprites_list.update()
        all_sprites_list.draw(screen)

        for i in range (0,ply_health-dmg_taken):  #heart
            screen.blit(heart, [10+20*(ply_health-1)*i,10])
        for i in range (0,dmg_taken):
            screen.blit(heart_empty,[10+20*(ply_health-1)*(ply_health-1-i),10])
        t1 = time.clock()
        t_dta = t1-t0

        fps_now = clock.get_fps()

        txt_fps = font.render('fps: '+ str(int(fps_now)),True,(255,255,255))
        txt_wave = font.render("Wave: " + str(wave), True, (255,255,255))
        txt_pwr = font.render("power: " + str(ply_power-1), True, (255,155,75))
        txt_scr_multi = font.render ('Score Multiplier: '+str(int(scr_multi*100)) +'%', True,(255,255,255))
        txt_wave_modifier = font.render ('wave mod: '+ str(wave_modifier),True,(255,255,255))
        txt_score = font.render('Score: '+str (int(score)), True, (215,85,255))
        txt_time_survive = font.render ('time you wasted: '+str(int(t_dta)), True, (230,150,200))

        if power_up_boo:
            txt_pwr_up = font.render('POWER UP !!!  + '+str(power_up_val), True, (230,170,100))
        screen.blit(txt_scr_multi,[30,90])
        screen.blit(txt_wave,[350,30])
        screen.blit(txt_wave_modifier,[350,70])
        screen.blit(txt_pwr,[350,50])
        screen.blit(txt_fps,[30,70])
        screen.blit(txt_score,[30,110])
        screen.blit(txt_time_survive,[30,130])
        if not power_up_frame == 0:
            screen.blit(txt_pwr_up,[100,50])
            power_up_frame += 1

        if power_up_frame == 300:
            power_up_frame = 0
        cycle+=1

        pygame.display.flip()
        clock.tick(fps)
        print('wait',wait,'cycle',cycle)

        if fps_now>0:
            last_fps = fps_now

    ##        rel = pygame.mouse.get_rel()
##        print('fps',clock.get_fps(),'recall',last_fps-fps_now,'set fps',fps,'difference',fps_now-fps)

    pygame.quit()

    print('score =',score)
    print('up to',wave,'waves')
    print('you survived',t_dta,'seconds')

    file_scr = open('scores.txt','a')
    inp = input('Your name')
    file_scr.write('\n'*2+'Player '+inp+'\n')
    file_scr.write('Score '+str (score)+'         '+'Up to Wave: '+str(wave)+'\n')
    file_scr.write('Time Survived'+str(t_dta)+'seconds'+'\n')
    file_scr.write('Time of entry-- ' + str(datetime.datetime.today())+'\n')
    file_scr.write('------------------------------------end of entry------------------------------------')
    file_scr.write('\n'*2)
    file_scr.close()


if __name__ == '__main__':
    main()

