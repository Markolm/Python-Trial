import pygame
from pygame.locals import *
pygame.init()

class Main(object):

    def __init__(self):
        pygame.display.set_caption("Moving Block")
        done = False
        screenSize = (640,480)
        surface = pygame.display.set_mode(screenSize)
        white = (255,255,255)
        player = Player()

        while not done:
            surface.fill(white)
            player.update(done)

            player.draw(surface)
            print(done)

            pygame.display.update()

class Player(object):
    
    def __init__(self):
                self.x = 0
		self.y = 0
		self.vx = 10
		self.vy = 10
        	self.size = (50,50)
        	self.color = (0,0,0)

    def update(self, result):
        global done
        controls = pygame.event.get()
        quitting = pygame.event.get()
        
        for e in controls:
            if e.type is KEYDOWN:

                if e.key == K_w:
                    if self.y > 0:
                        self.vy = -10
                        self.y += self.vy

                if e.key == K_d:
                    if self.x < 640:
                        self.vx = 10
                        self.x += self.vx

                if e.key == K_s:
                    if self.y < 480:
                        self.vy = 10
                        self.y += self.vy

                if e.key == K_a:
                    if self.x > 0:
                        self.vx = -10
                        self.x += self.vx

        for e in quitting:
            if e.type is KEYDOWN:
                if e.key == K_q:
                    result = True

            if e.type is QUIT:
                    result = True

            else:
                result = False

        return(result)


    def draw(self, surface):
        rect = pygame.Rect((self.x, self.y), self.size)
        pygame.draw.rect(surface, self.color, rect)
		
Main()
	
