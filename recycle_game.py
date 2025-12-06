import pygame
import time
import random
from pygame.locals import*
pygame.init()
pygame.display.set_caption("recycle")
width=1000
height=800
screen=pygame.display.set_mode([width,height])
#varibles 
run=True
score=0
start=time.time()
font=pygame.font.SysFont("pressure",20)
fontt=pygame.font.SysFont("opera",15)
#bg=pygame.image.load(r"/home/asmee/projects/jetleran/Pygame/Recycle/recycle_bg.jpg")
clock=pygame.time.Clock()
#bin object class
class bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("bin.png")
        self.image=pygame.transform.scale(self.image,(150,140))
        self.rect=self.image.get_rect()
#cLass for recycleable items
class rec(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image,(80,80))
        self.rect=self.image.get_rect()
        
#creating bin object
recimg=["glass.png","paperbag.png","woodenbox.png"]
recgrp=pygame.sprite.Group()
nonrecgrp=pygame.sprite.Group()
imgall=pygame.sprite.Group()
for i in range(30):
    objrec=rec(random.choice(recimg))
    objrec.rect.x=random.randint(10,950)
    objrec.rect.y=random.randint(10,730)
    recgrp.add(objrec)
    imgall.add(objrec)
#class for non-recycleable items
class nonrec(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("plasticbag.png")
        self.image=pygame.transform.scale(self.image,(80,80))
        self.rect=self.image.get_rect()
for i in range(15):
    nonobj=nonrec()
    nonobj.rect.x=random.randint(10,950)      
    nonobj.rect.y=random.randint(10,730) 
    nonrecgrp.add(nonobj)
    imgall.add(nonobj)
binimg=bin()
imgall.add(binimg)
#bg function
def bgd(img):
    loaded=pygame.image.load(img)
    img1=pygame.transform.scale(loaded,(width,height))
    screen.blit(img1,(0,0))
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    #checking if time>60 seconds
    totaltime=time.time()-start
    if totaltime>=60:
        if score>20:
            bgd("win_bg.png")
        else:
            bgd("lose_bg.png")
    else:
        
        bgd("recycle_bg.jpg")
        #bin movement
        keys=pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            #if binimg.rect.y>=0:
                binimg.rect.y+=10
        if keys[pygame.K_UP]:
            #if binimg.rect.y<=height:
                binimg.rect.y-=10
        if keys[pygame.K_LEFT]:
            #if binimg.rect.x>=0:
                binimg.rect.x-=10
        if keys[pygame.K_RIGHT]:
        # if binimg.rect.x<=width:
                binimg.rect.x+=10
        imgall.draw(screen)
    pygame.display.update()
pygame.quit()
