import pygame
import time
import random
from pygame.locals import*
pygame.init()
pygame.display.set_caption("recycle")
width=800
height=800
screen=pygame.display.set_mode([width,height])
#varibles 
run=True
score=0
start=time.time()
font=pygame.font.SysFont("pressure",20)
fontt=pygame.font.SysFont("opera",15)
bg=pygame.image.load("recycle_bg.jpg")
clock=pygame.time.Clock()
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
    bgd(bg)
    pygame.display.update()
pygame.quit()
