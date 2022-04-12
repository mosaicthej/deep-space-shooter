#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      5604254
#
# Created:     26/03/2018
# Copyright:   (c) 5604254 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

##import pygame,math, os
##
##_image_library = {}
##def get_image(path):
##        global _image_library
##        image = _image_library.get(path)
##        if image == None:
##                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
##                image = pygame.image.load(canonicalized_path)
##                _image_library[path] = image
##        return image
##
##pygame.init()
##screen = pygame.display.set_mode((960, 400))
##done = False
##clock = pygame.time.Clock()
##
##while not done:
##        for event in pygame.event.get():
##                if event.type == pygame.QUIT:
##                        done = True
##
##        screen.fill((255, 255, 255))
##
##        screen.blit(get_image('background01.png'), (0,0))
##
##        pygame.display.flip()
##        clock.tick(60)
import pygame,os,random,math,copy
die1,die2, space = False, False,False
thug = 0
pygame.init()
bgm,thugbgm,gg= 'mario theme song.ogg','next-ep.ogg','game-over_01.ogg'
#bgm = pygame.mixer.Sound('mario theme song.ogg')
def sound(call,name):
    call = pygame.mixer.Sound(name)


sound(bgm, 'mario theme song.ogg')
sound(thugbgm,'next-ep.ogg')
sound(gg,'game-over_01.ogg')

bgx,bgsec = 0,959

y_coord, y_speed = 100, 0
y2_cor, y2_spd= 100,0
x2_cor= 100
print("output only used for debug")


txt = ''
font = pygame.font.SysFont('Calibri', 25, True, False)
text = font.render(txt,True,(0,0,0))

color = pygame.Color
draw = pygame.draw
done = False
clock = pygame.time.Clock()
pi = math.pi
pipColor = (15,106,58)
tick = 24

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
            _image_library[path] = image
    return image

"""paper"""
pipC = 20
lista,listb,listlen,pipList = [],[],[],[]
for i in range(0,7):
    pipLen = random.randint(0,235)
    pipA = random.randint(0,pipLen)
    pipB = pipLen -pipA
    listlen.append(pipLen)
    lista.append(pipA)
    listb.append(pipB)

    x = 160*i
    y=0
    pipList.append([x,y])


"""paper end"""

size = (1500,400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bird")

done = False
fps = pygame.time.Clock()

def draw_pipe(x,ind):
##
##    pipC = 20
##    pipLen = random.randint(0,235)
##    pipA = random.randint(0,pipLen)
##    pipB = pipLen -pipA
    global lista, listb, listlen
    pa = lista[ind]
    pb = listb[ind]
    plen = listlen[ind]
    #up pipe
    draw.rect(screen,pipColor,[x,0,50,pa])#var
    draw.rect(screen,pipColor,[x-5,pa,60,20])#end

    # book keeping purpose
##    screen.blit(text,[x,50])
    #pipe down
    draw.rect(screen,pipColor,[x,325-pb,50,pb])#var
    draw.rect(screen,pipColor,[x-5,305-pb,60,20]) #end
wingn,wing = -1,-1

def draw_bird(x,y):
    #wing  = random.randint(1,4)
    global wing, die1
    wing += 1
    if die1 == False:
        if thug>5:
            screen.blit(get_image('bird_000%d-thug.png' %(wing)),(x,y))
        elif space and thug<=5:
            screen.blit(get_image('bird_000%d-drop.png' %(wing)),(x,y))
        else:
            screen.blit(get_image('bird_000%d.png' %(wing)),(x,y))

##        if wing == 1:
##            screen.blit(get_image('bird_0000.png'), (x,y))
##        if wing == 2:
##            screen.blit(get_image('bird_0001.png'), (x,y))
##        if wing == 3:
##            screen.blit(get_image('bird_0002.png'), (x,y))
##        if wing == 4:
##            screen.blit(get_image('bird_0003.png'), (x,y))
        if wing >= 3:
            wing = 0
    elif die1 == True:
        screen.blit(get_image('bird_dead.png'), (x,y))

##    if die1 == True:
##
##    if wing > 4:
##        wing =0
    ##print (die1)


def draw_second_bird(x,y):
    global wingn
    wingn += 1
    #print(wingn)
    screen.blit(get_image('nbird_000%d.png' %(wingn)),(x,y))
##    if wingn == 1:
##        screen.blit(get_image('nbird_0000.png'), (x,y))
##    elif wingn == 2:
##        screen.blit(get_image('nbird_0001.png'), (x,y))
##    elif wingn == 3:
##        screen.blit(get_image('nbird_0002.png'), (x,y))
##    elif wingn == 4:
##        screen.blit(get_image('nbird_0003.png'), (x,y))
    if wingn >= 3:
        wingn = 0



ybird = 200
txt = ''

fly_sound = pygame.mixer.Sound("crow.ogg")

if thug<5 and not die1:
##    pygame.mixer.music.load('mario theme song.ogg')
    pass
elif thug>=5 and not die1:
    pygame.mixer.music.load('next-ep.ogg')
elif die1:
    pygame.mixer.music.load('game-over01.ogg')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
##pygame.mixer.music.play()

# -------- Main Program Loop -----------

while not done:
    text = font.render(txt,True,(0,0,0))
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.constants.USEREVENT and not done:
            if thug<5 and not die1:
##                pygame.mixer.music.load('mario theme song.ogg')
##                pygame.mixer.music.play()
                pass
            elif thug>=5 and not die1:
                pygame.mixer.music.load('next-ep.ogg')
                pygame.mixer.music.play()
            elif die1:
                pygame.mixer.music.load('game-over_01.ogg')
                pygame.mixer.music.play()

        elif die1 == False:
            if event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.

                if event.key == pygame.K_SPACE:
                    fly_sound.set_volume(.2)
                    fly_sound.play()
                    y_speed = 10
                    space = True

            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero

               if event.key == pygame.K_SPACE:
                    y_speed = 0
                    space = False

        elif die1 == True:

            y_speed = -5
            if event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.

                if event.key == pygame.K_SPACE:
                    y_speed = -5
            # User let up on a key
            if event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
               if event.key == pygame.K_SPACE:
                    y_speed = -5
# control for bird 2
##        elif die2 == False:
##            if event.type == pygame.


##        # User let up on a key
##        elif event.type == pygame.KEYUP:
##            # If it is an arrow key, reset vector back to zero
##
##           if event.key == pygame.K_SPACE:
##                y_speed = 0





    # --- Game logic should go here
            # Move the object according to the speed vector.
    if y_coord<305:
        y_coord -= y_speed
        y_coord += 5

    elif y_coord >= 305:
        y_coord = 305

    pos = pygame.mouse.get_pos()
    y2_cor = pos[1]
    x2_cor = pos[0]

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    screen.fill((255,255,255))
    #original background image
    #screen.blit(get_image('background01.png'), (0,0))
    screen.blit(get_image('bg_down.png'),(bgx,0))
    screen.blit(get_image('bg_sky.png'),(bgx,0))
    screen.blit(get_image('bg_down.png'),(bgsec,0))
    screen.blit(get_image('bg_sky.png'),(bgsec,0))
    bgx -=1
    bgsec-= 1
    #print(bgx,bgsec)
    if bgx< -959:
        bgx = 0
    if bgsec<0:
        bgsec = 959



##    for i in range (1,4):
##        screen.blit(get_image('bird%d.png'%(i)),(0,200))
    # --- Drawing code should go here
    ##background = pygame.image.load(background.png)
##    for i in range (0,13):
##        xpos = xlist [i]
##        draw_pipe(xpos,i)

    #draw.rect(screen,(255,199,16),[20,ybird,30,30])
    for pips in range(len(pipList)):
        global y_coord
##        x = copy.copy(i)*80+5
        draw_pipe(pipList[pips][0],pips)
        pipList[pips][0] -= 60/tick


##        if snow_list[i][1] > 400:
##            # Reset it just above the top
##            y = random.randrange(-50, -10)
##            snow_list[i][1] = y
##            # Give it a new x position
##            x = random.randrange(0, 400)
##            snow_list[i][0] = x
##        pipColorL = list(pipColor)
##        delcol = 5
##        pipColorL[1] += delcol
##
##        if pipColorL[1]< 10 or pipColorL[1]>250:
##            delcol = - delcol
##        pipColor = tuple(pipColorL)

        if pipList[pips][0] < -55:
            listlen[pips] = random.randint(0,235)
            lista[pips] = random.randint(0,listlen[pips])
            listb[pips] = listlen[pips]-lista[pips]

            ##            for incr in range (0,13):
##                pipLen = random.randint(0,235)
##                pipA = random.randint(0,pipLen)
##                pipB = pipLen - pipA
##                lista.append(pipA)
##                listb.append(pipB)
##                listlen.append(pipLen)
            pipList[pips][0] = 1095

#commented out part for animation
            pip_for_bird1 = pips
            txt = str(pip_for_bird1)
            yspace = (305-listb[pip_for_bird1-2])-(lista[pip_for_bird1-2]+20)     #C ON PAPRER
##            print (pips)
##            print(yspace, ycoord)

            y1up = listb[pip_for_bird1]+20
            y1down = y1up+yspace
            if y_coord not in range(y1up,y1down):
                die1 = True
                thug = 0
            if not die1:
                thug +=5


##            ypt =(305-listb[pip_for_bird])-yspace
##            ypt = ypt +int(yspace/2)
##            ydisp = ypt-ybird
##            yspeed = ydisp/tick
            #print(y1down,y1up,y_coord)
            #print(die1)
##            ybird += yspeed*tick
##            ybird = int(ybird)
#kill bird if it's dead

        #draw.circle(screen,(0,0,0),[50,ybird+25],15)
        draw_bird(50,y_coord)
        #draw_bird(40,300)
        #draw_second_bird(500,y2_cor)
        #draw_second_bird(x2_cor,y2_cor+50)



##    for item in pipList:
####        xpos = item[0]
####        xpos -=1
##        item[0] -= 1
##        ind = int(item[0]/80)
##        draw_pipe(item[0],ind)
##
##        if item[0]<-55:
##            item[0] = 975
##            pipLen = random.randint(0,235)
##            pipA = random.randint(0,pipLen)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    #print(die1)
    print(thug)

    # --- Limit to 60 frames per second
    fps.tick(tick)

# Close the window and quit.
pygame.quit()