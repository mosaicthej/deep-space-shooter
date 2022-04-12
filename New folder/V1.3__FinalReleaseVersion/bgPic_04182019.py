#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      5604254
#
# Created:     18/04/2019
# Copyright:   (c) 5604254 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()



import math
import random
import os,pygame,time,datetime
import classes_vX3
import otherCodesThatsUseful as ocu
import PIL

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
