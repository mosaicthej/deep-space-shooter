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
import pygame
pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self,color, x, y,size = [15,15]):
        super().__init__()

        self.image = pygame.Surface(size)
        self.image.fill(color)

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

    def __init__(self,color,x,y,width,height):

        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0

class Bullet(pygame.sprite.Sprite):

    def __init__(self,color,x,y,speed,size=[5,5]):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = speed

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
