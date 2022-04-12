import pygame,random,os
# Initialize Pygame
pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)


_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
            _image_library[path] = image
    return image

px,py = 350,200
clr = (20,50,70)

##coin = pygame.image.load("pycoin.png").convert()
##coinogg = pygame.mixer.Sound("coin.ogg")
##crow = pygame.mixer.Sound("crow.ogg")

##class Block(pygame.sprite.Sprite):
##    """
##    This class represents the ball.
##    It derives from the "Sprite" class in Pygame.
##    """
##
##    def __init__(self):
##        """ Constructor. Pass in the color of the block,
##        and its x and y position. """
##
##        # Call the parent class (Sprite) constructor
##        super().__init__()
##
##        # Create an image of the block, and fill it with a color.
##        # This could also be an image loaded from the disk.
##        self.image = pygame.Surface([20,20])
##        self.image.fill((200,35,45))
####        self.image.fill(color)
##
##        # Fetch the rectangle object that has the dimensions of the image
##        # image.
##        # Update the position of this object by setting the values
##        # of rect.x and rect.y
##        self.rect = self.image.get_rect()
##
##
##class bad_block(pygame.sprite.Sprite):
##    def __init__(self, color, width, height):
##        # Call the parent class (Sprite) constructor
##        super().__init__()
##
##        # Create an image of the block, and fill it with a color.
##        # This could also be an image loaded from the disk.
##        self.image = pygame.Surface([width, height])
##        self.image.fill(color)
##
##        # Fetch the rectangle object that has the dimensions of the image
##        # image.
##        # Update the position of this object by setting the values
##        # of rect.x and rect.y
##        self.rect = self.image.get_rect()





class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([50,100])
##        self.r,self.g,self.b = 200,50,70
##        self.image.fill((self.r,self.g,self.b))

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.x > screen_width:
            self.rect.x = 0
        if self.rect.x <0:
            self.rect.x = screen_width
        if self.rect.y> screen_height:
            self.rect.y = 0
        if self.rect.y< 0:
            self.rect.y = screen_height

class Hitbox(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([10,10])
        self.r,self.g,self.b = 255,255,255
        self.image.fill((self.r,self.g,self.b))

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.x > screen_width:
            self.rect.x = 0
        if self.rect.x <0:
            self.rect.x = screen_width
        if self.rect.y> screen_height:
            self.rect.y = 0
        if self.rect.y< 0:
            self.rect.y = screen_height






# Set the height and width of the screen


# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
badBlock_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()



plr = Player(px,py)
hbx = Hitbox(px+25+40,py+50+40)
##all_sprites_list.add(plr,hbx)
ply_con = pygame.sprite.Group()
ply_con.add(plr,hbx)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

##score = 0


picSerie = 0
picLyr = 18
# -------- Main Program Loop -----------

while not done:

    picSerie += 1
    picLyr -= 1
    if picSerie >17:
        picSerie = 0
    if picLyr < 1:
        picLyr = 18
    if picSerie<10:
        picstr = 'plane01_000'+str(picSerie)+'_Layer-'+str(picLyr)+'.png'
    elif picSerie >=10:
        picstr = 'plane01_00'+str(picSerie)+'_Layer-'+str(picLyr)+'.png'


    plane00pic = get_image(picstr)
    print(picSerie)

    plr.image = plane00pic
##    plr.rect = plr.image.get_rect()

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

    # Clear the screen
    #screen.fill(((random.randint(0,255),random.randint(0,255),random.randint(0,255))))
    screen.fill(WHITE)

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()

    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
##    player.rect.x = pos[0]
##    player.rect.y = pos[1]

    # See if the player block has collided with anything.
##    blocks_hit_list = pygame.sprite.spritecollide(block_list,plr, True)
    blocks_hit_list = pygame.sprite.spritecollide(hbx, block_list, True)
    naughty_list =pygame.sprite.spritecollide(hbx, badBlock_list, True)
    # Check the list of collisions.
    for block in blocks_hit_list:
##        coinogg.play()
##        score += 1
##        print(score)
        pass


    for block in naughty_list:
##        crow.play()
##        if  score >= 1:
##            score -= 1
##
##        print(score)
        pass


    # Draw all the spites
    ply_con.draw(screen)
##    for blk in badBlock_list:
##        blk.image.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    plr.update()
    hbx.update()

##    font = pygame.font.SysFont('Calibri', 25, True, False)
##    text = font.render('score'+str(score),True,(200,98,198))
##    screen.blit(text,[250,10])
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
