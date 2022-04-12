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


import random,os ,pygame,PIL
from PIL import Image

def randhexstr(len):   #a function that give a random hex for a given length"""
    hexl = []
    for i in range (10):
        hexl.append(i)

    let = ['a','b','c','d','e','f']
    for l in let:
        hexl.append(l)

    outL = []
    for i in range(len):
        outL.append(random.choice(hexl))

    outS = '#'
    for l in outL:
        outS = outS+str(l)

    return outS

def randrgb(r=-1,g=-1,b=-1):
    if r not in range(0,255):
        r = random.randint(0,255)
    if g not in range(0,255):
        g = random.randint(0,255)
    if b  not in range(0,255):
        b = random.randint(0,255)
    return(r,g,b)


def get_image(path):
    _image_library = {}
    image = _image_library.get(path)
    if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
            _image_library[path] = image
    return image

def rgb_2_hsv(rgbList):
    R,G,B = rgbList[0]/255,rgbList[1]/255,rgbList[2]/255
    Cmx,Cmn = max(R,G,B), min(R,G,B)
    dta = Cmx-Cmn

    #hue:
    if dta == 0:
        h = 0
    elif Cmx == R:
        h = 60* ( ( (G-B)/dta) %6)
    elif Cmx == G:
        h = 60* ( ( (B-R)/dta) +2)
    elif Cmx == B:
        h = 60* ( ( (R-G)/dta) +4)

    if Cmx == 0:
        s = 0
    else:
        s = dta/ Cmx

    v = Cmx

    hsv = [int(h),s,v]
    return hsv

def hsv_2_rgb(hsvList):
    h,s,v = hsvList[0],hsvList[1],hsvList[2]
    c = v*s
    x = c* (1- abs((h/60)% 2 -1) )
    m = v-c

    h = h %360

    if 0<=h<60:
        rgb = [c,x,0]
    elif 60<=h<120:
        rgb = [x,c,0]
    elif 120<=h<180:
        rgb = [0,c,x]
    elif 180<=h<240:
        rgb = [0,x,c]
    elif 240<=h<300:
        rgb = [x,0,c]
    elif 300<=h<360:
        rgb = [c,0,x]

    r,g,b = (rgb[0]+m)*255, 255*(rgb[1]+m),255*(rgb[2]+m)
    rgb =[int(r),int(g),int(b)]
    return rgb



def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)


def hueShift (img_path, shift):
    img = Image.open(img_path)
    img = img.convert('RGBA')
    pix = img.load()
    pix_pos, pix_rgb, pix_alpha = [],[],[]
    w, h = img.size[0],img.size[1]

    for x in range (1,w):

        for y in range (1,h):
            pix_pos.append([x,y])
            r,g,b,a = pix[x,y][0], pix[x,y][1], pix[x,y][2], pix[x,y][3]
            pix_rgb.append([r,g,b])
            pix_alpha.append(a)

    pix_hsv = []
    for r in pix_rgb:
        pix_hsv.append(rgb_2_hsv(r))
    new_hsv = []
    for oh in pix_hsv:
        nh = oh[0]+shift
        new_hsv.append([nh,oh[1],oh[2]])
    new_rgb = []
    for n in new_hsv:
        new_rgb.append(hsv_2_rgb(n))

    new_img = PIL.Image.new('RGBA',(w,h))

    new_rgba = []

    for i in range (0,len(pix_alpha)-1):
        rgba = (new_rgb[i][0],new_rgb[i][1],new_rgb[i][2],pix_alpha[i])
        new_rgba.append(rgba)

    new_img.putdata(new_rgba)

    return new_img




