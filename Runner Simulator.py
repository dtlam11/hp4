import pygame
import os
import math
#Khởi tạo thư viện pygame
pygame.init()
#Tạo cửa sổ window với width và height
W, H = 800, 447
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Background Scrolling')
bg = pygame.image.load(os.path.join('images', 'bg.jpg')).convert()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()

class player(object):
    run = [pygame.image.load(os.path.join('images', str(x) + '.png'))for x in range(8, 16)]
    jump = [pygame.image.load(os.path.join('images', str(x) + '.png'))for x in range(1, 8)]
    slide = [pygame.image.load(os.path.join('images', 'S1.png')), pygame.image.load
    (os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png'))
    , pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png'))
    , pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png'))
    , pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png'))
    , pygame.image.load(os.path.join('images', 'S3.png')), pygame.image.load(os.path.join('images', 'S4.png'))
    , pygame.image.load(os.path.join('images', 'S5.png'))]
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,
                4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                -1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,
                -4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False
    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount//18], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                    self.jumpCount = 0
                    self.jumping = False
                    self.runCount = 0
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                    self.y += 1
            elif self.slideCount == 80:
                    self.y -= 19
                    self.sliding = False
                    self.slideUp = True
            if self.slideCount >= 110:
                    self.slideCount = 0
                    self.slideUp = False
                    self.runCount = 0
            win.blit(self.slide[self.slideCount//10], (self.x,self.y))
            self.slideCount += 1
        else:
            if self.runCount > 42:
                    self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x,self.y))
            self.runCount += 1

runner = player(200, 313, 64, 64)

def redrawWindow():
    win.blit(bg, (bgX, 0))  
    win.blit(bg, (bgX2, 0))
    runner.draw(win)
    pygame.display.update()

run = True
speed = 5

while run:
    redrawWindow()
    bgX -= 0.2
    bgX2 -= 0.2

    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              run = False
              pygame.quit()
              quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]: # If user hits space or up arrow key
        if not(runner.jumping):  # If we are not already jumping
            runner.jumping = True

    if keys[pygame.K_DOWN]:  # If user hits down arrow key
        if not(runner.sliding):  # If we are not already sliding
            runner.sliding = True

