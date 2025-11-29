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
#creating bin object
binimg=bin()
imgall=pygame.sprite.Group()
imgall.add(binimg)
#class for non-recycleable items

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
