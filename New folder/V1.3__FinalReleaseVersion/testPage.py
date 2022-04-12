#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      5604254
#
# Created:     14/05/2018
# Copyright:   (c) 5604254 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import playerClass as pc
import pygame,random

pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)


px,py = random.randrange(screen_width),random.randrange(screen_height)

plr = pc.Player(px,py)
hbx = pc.Hitbox(px+25,py+50)

ply_con = pygame.sprite.Group()
ply_con.add(plr,hbx)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        for ply in ply_con:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ply.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    ply.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    ply.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    ply.changespeed(0, 3)
##            plr.image.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

        # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ply.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    ply.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    ply.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    ply.changespeed(0, -3)

    screen.fill(WHITE)
    ply_con.draw(screen)

    for sp in ply_con:
        sp.update()


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
