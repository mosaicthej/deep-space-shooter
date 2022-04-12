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
import pygame, math, random ,otherCodesThatsUseful as ocu
pygame.init()

WHITE = (255,255,255)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,127,0)
TEAL = (0,255,200)
PINK = (255, 186, 209)

height = 800
width = 550

bullet_str_lst = ['bullet_0000_Hue_Saturation-1-copy-5.png','bullet_0001_Hue_Saturation-1-copy-4.png','bullet_0002_Hue_Saturation-1-copy-3.png','bullet_0003_Hue_Saturation-1-copy-2.png','bullet_0004_Hue_Saturation-1-copy.png']
bullet_img_lst = []

print('loading bullets......')
for st in bullet_str_lst:
    bullet_img_lst.append(ocu.get_image(st))


class Player(pygame.sprite.Sprite):

    def __init__(self,color, x, y):
        super().__init__()

        self.image = pygame.Surface([15,15])
        self.image.fill(color)

        self.damage_taken = 0

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

class Enemy(pygame.sprite.Sprite):

    def __init__(self,image,color,x,y,width,height,max_health,speed,damage_taken,health_bar_length,number_bullets,cycle_length):

        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        if image == 0:
            self.image = pygame.Surface([self.width,self.height])
            self.image.fill(color)
        else:
            self.image = image

        self.length = health_bar_length
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.max_health = max_health
        self.damage_taken = damage_taken
        self.change_x = speed
        if speed == 0:
            self.change_y = speed
        else:
            self.change_y = math.floor(speed/10) +1
        self.random_increment = random.randint(1,500)
        self.random_cycle_increment = random.randint(1,500)
        self.number_bullets = number_bullets
        self.cycle_length = cycle_length

        self.random_increment = random.randint(1,500)
        self.random_cycle_increment = random.randint(1,500)
        self.screen_height = random.randint(50,150)
        self.acceleration = 0.5
        self.speed = 0
        self.bullet_list = []
        self.shoot_count = 0

    def draw_health(self,screen):
        bar_x = self.rect.x + self.width/2 - (self.length)/2
        bar_y = self.rect.y -17
        pygame.draw.rect(screen, WHITE, [bar_x-1,bar_y-1,self.length+2,13])
        health_percent = (self.max_health - self.damage_taken)/self.max_health
        for i in range(math.floor(self.length*(health_percent))):
            BAR = (255 - 255 * (i/self.length*(health_percent)),0 + 255 * (i/self.length*(health_percent)),0)
            pygame.draw.line(screen,BAR,[bar_x+i,bar_y],[bar_x+i,bar_y+10])

    def destroy(self):
        self.kill()
        self.width = 0
        self.height = 0
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill((0,0,0))
        self.length = 0
        self.max_health = 0
        self.damage_taken =0
        self.change_x = 0
        self.change_y = 0

    def update_enemy(self,cycle):
        self.cycle = cycle+ self.random_increment
        if self.rect.y < 25:
            self.rect.y += self.change_y
        if self.change_x == 0:
            self.rect.x += self.change_x
        else:
            if ((self.cycle) % (2* ((width - self.width)//self.change_x))) == (self.cycle) % ((width - self.width)//self.change_x):
                self.rect.x = 0 + self.change_x *((self.cycle) % (math.floor((width - self.width)/self.change_x)))
            else:
                self.rect.x = ( width - self.width) - self.change_x * ((self.cycle) % (math.floor((width - self.width)/self.change_x)))

    def shoot_enemy(self, cycle, player_x, player_y):
        self.cycle = cycle
        if (self.cycle + self.random_cycle_increment) % self.cycle_length == 0:
            self.bullet_list = []
            for i in range (self.number_bullets):
                bullet_speed_rnd_00 = random.randint(2,6)
                bullet_clr_rnd_00 = (230-30*bullet_speed_rnd_00,30*bullet_speed_rnd_00,30*bullet_speed_rnd_00)
                bullet = Bullet((250,100,215),(self.rect.x + (i+1)/(self.number_bullets+1)*self.width),(self.rect.y + self.height),0,bullet_speed_rnd_00)
                self.bullet_list.append(bullet)
    def draw(self,screen):
        screen.blit(self.image,[self.rect.x,self.rect.y])


class Bullet(pygame.sprite.Sprite):

    def __init__(self,color,x,y,change_x,change_y,size=[5,5]):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        if color == YELLOW:
            self.image = bullet_img_lst[2]
        elif color == TEAL:
            self.image = bullet_img_lst[0]
        elif color == PINK:
            self.image = bullet_img_lst[3]
        elif color == ORANGE:
            self.image = ocu.get_image(random.choice(['flag01.png','flag.png','flag@0,5x.png']))

        self.rect.x = x
        self.rect.y = y
        self.change_x = change_x
        self.change_y = change_y

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.x > 600 or self.rect.x<-100 or self.rect.y>900 or self.rect.y<-100:
            self.kill()


##class Bomb(pygame.sprite.Sprite):


##class Item (pygame.sprite.Sprite):  #class for
##    def __init__(self,fx):
##        super().__init__()
##        self.width,self.height = 40,40
##        self.image = ocu.get_image(str(fx)+'.png')

class Bird(Enemy):

    def update_enemy(self,cycle):
        self.cycle = cycle + self.random_increment
        if self.rect.y < 25:
            self.rect.y += self.change_y
        else:
            self.rect.y = 50*math.sin(self.cycle/50) + 100
        if self.change_x == 0:
            self.rect.x += self.change_x
        else:
            if ((self.cycle) % (2* ((width - self.width)//self.change_x))) == (self.cycle) % ((width - self.width)//self.change_x):
                self.rect.x = 0 + self.change_x *((self.cycle) % (math.floor((width - self.width)/self.change_x)))
            else:
                self.rect.x = ( width - self.width) - self.change_x * ((self.cycle) % (math.floor((width - self.width)/self.change_x)))

    def shoot_enemy(self, cycle, player_x, player_y):

        self.cycle = cycle + self.random_increment
        if (self.cycle) % self.cycle_length == 0:
            self.bullet_list = []
            for i in range (self.number_bullets):
                cycle_angle =(cycle % 157)/100
                cycle_angle2 =(cycle % 314)/100
                if cycle_angle ==  cycle_angle2:
                    angle = cycle_angle - math.pi/4
                else:
                    angle = -(cycle_angle - math.pi/4)
                bullet_speed_rnd_00 = 5
                bullet_speed_rnd_00_x = -bullet_speed_rnd_00 * math.sin(angle)
                bullet_speed_rnd_00_y = bullet_speed_rnd_00 * math.cos(angle)
                bullet_clr_rnd_00 = (255-30*bullet_speed_rnd_00,30*bullet_speed_rnd_00,30*bullet_speed_rnd_00)
                bullet = Bullet(YELLOW,(self.rect.x + (i+1)/(self.number_bullets+1)*self.width),(self.rect.y + self.height),bullet_speed_rnd_00_x,bullet_speed_rnd_00_y)
                self.bullet_list.append(bullet)

class Ghost(Enemy):

    def update_enemy(self,cycle):
        self.cycle = cycle + self.random_increment

        if self.cycle % (2*self.cycle_length) == 0:
            self.rect.x = random.randint(0,width-self.width)
            self.rect.y = random.randint(50,150)

    def shoot_enemy(self, cycle, player_x, player_y):

        self.cycle = cycle + self.random_increment
        if (self.cycle) % self.cycle_length == math.floor(self.cycle_length/2):
            self.bullet_list = []
            for i in range (self.number_bullets):
                dist_x = (self.rect.x+self.width/2)-player_x
                dist_y = (self.rect.y)-player_y
                angle = math.atan(dist_x/dist_y)
                bullet_speed_rnd_00 = 5
                bullet_speed_rnd_00_x = bullet_speed_rnd_00 * math.sin(angle)
                bullet_speed_rnd_00_y = bullet_speed_rnd_00 * math.cos(angle)
                bullet_clr_rnd_00 = (255-30*bullet_speed_rnd_00,30*bullet_speed_rnd_00,30*bullet_speed_rnd_00)
                bullet = Bullet(PINK,(self.rect.x + (i+1)/(self.number_bullets+1)*self.width),(self.rect.y + self.height),bullet_speed_rnd_00_x,bullet_speed_rnd_00_y)
                self.bullet_list.append(bullet)

class Hog(Enemy):


    def update_enemy(self,cycle):
        self.cycle = cycle + self.random_increment
        self.speed+= self.change_x*self.acceleration/10
        if self.rect.y < 25:
            self.rect.y += self.change_y
        else:
            self.rect.y = self.screen_height
        if 0<self.rect.x + self.speed < width-self.width:
            self.rect.x += self.speed
        else:
            self.acceleration = self.acceleration*(-1)
            self.speed = 0

    def shoot_enemy(self, cycle, player_x, player_y):

        self.cycle = cycle + self.random_increment
        if (self.cycle) % self.cycle_length == math.floor(self.cycle_length/2):
            self.bullet_list = []
            for i in range (self.number_bullets):
                bullet_speed_rnd_00 = random.randint(2,6)
                bullet_speed_rnd_00_x = 0
                bullet_speed_rnd_00_y = bullet_speed_rnd_00
                bullet_clr_rnd_00 = (255-30*bullet_speed_rnd_00,30*bullet_speed_rnd_00,30*bullet_speed_rnd_00)
                bullet = Bullet(TEAL,(self.rect.x + (i+1)/(self.number_bullets+1)*self.width),(self.rect.y + self.height),bullet_speed_rnd_00_x,bullet_speed_rnd_00_y)
                self.bullet_list.append(bullet)

class Boss (Enemy):

    def draw_health(self,screen):
        bar_x = self.rect.x + self.width/2 - (self.length)/2
        bar_y = self.rect.y + self.height +4
        pygame.draw.rect(screen, WHITE, [bar_x-1,bar_y-1,self.length+2,13])
        health_percent = (self.max_health - self.damage_taken)/self.max_health
        for i in range(math.floor(self.length*(health_percent))):
            BAR = (255 - 255 * (i/self.length*(health_percent)),0 + 255 * (i/self.length*(health_percent)),0)
            pygame.draw.line(screen,BAR,[bar_x+i,bar_y],[bar_x+i,bar_y+10])


    def shoot_enemy(self, cycle, player_x, player_y):

        self.cycle = cycle + self.random_increment
        if (self.cycle) % self.cycle_length == math.floor(self.cycle_length/2):
            self.bullet_list = []
            self.shoot_count+=1
            for i in range (self.number_bullets):
                bullet_angle = (i+1)*(180/(self.number_bullets+1))
                bullet_speed_rnd_00 = random.randint(3,5)
                bullet_speed_rnd_00_x = bullet_speed_rnd_00 * math.cos(bullet_angle)
                bullet_speed_rnd_00_y = -bullet_speed_rnd_00 * math.sin(bullet_angle)
                bullet_clr_rnd_00 = (255-30*bullet_speed_rnd_00,30*bullet_speed_rnd_00,30*bullet_speed_rnd_00)
                bullet = Bullet(ORANGE,(self.rect.x + self.width/2),(self.rect.y + self.height),bullet_speed_rnd_00_x,bullet_speed_rnd_00_y)
                self.bullet_list.append(bullet)



