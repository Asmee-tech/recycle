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
fontt=pygame.font.Sysfont("opera",15)
bg=pygame.image.load("recycle_bg.jpg")
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()