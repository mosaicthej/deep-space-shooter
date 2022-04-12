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
import pygame, otherCodesThatsUseful as ocu, math, random
pygame.init()

WHITE = (255,255,255)
BLUE = (0,0,255)

height = 800
width = 550

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

        self.bullet_list = []

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

    def shoot_enemy(self, cycle):
        self.cycle = cycle
        if (self.cycle + self.random_cycle_increment) % self.cycle_length == 0:
            self.bullet_list = []
            for i in range (self.number_bullets):
                bullet_speed_rnd_00 = random.randint(2,7)
                bullet_clr_rnd_00 = (255-30*bullet_speed_rnd_00,30*bullet_speed_rnd_00,30*bullet_speed_rnd_00)
                bullet = Bullet(bullet_clr_rnd_00,(self.rect.x + (i+1)/(self.number_bullets+1)*self.width),(self.rect.y + self.height),bullet_speed_rnd_00)
                self.bullet_list.append(bullet)

class Bullet(pygame.sprite.Sprite):

    def __init__(self,color,x,y,speed,size=[5,5]):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.change_x = 0
        self.change_y = speed

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

##class Bomb(pygame.sprite.Sprite):


class Item (pygame.sprite.Sprite):  #class for
    def __init__(self,fx):
        super().__init__()
        self.width,self.height = 40,40
        self.image = ocu.get_image(str(fx)+'.png')

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

    def shoot_enemy(self, cycle):

        self.cycle = cycle
        if (self.cycle + self.random_cycle_increment) % self.cycle_length == 0:
            self.bullet_list = []
            for i in range (self.number_bullets):
                bullet_speed_rnd_00 = random.randint(2,7)
                bullet_clr_rnd_00 = (255-30*bullet_speed_rnd_00,30*bullet_speed_rnd_00,30*bullet_speed_rnd_00)
                bullet = Bullet(bullet_clr_rnd_00,(self.rect.x + (i+1)/(self.number_bullets+1)*self.width),(self.rect.y + self.height),bullet_speed_rnd_00)
                self.bullet_list.append(bullet)

