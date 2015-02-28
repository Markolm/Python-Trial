import time
import pygame
from pygame.locals import *
pygame.init()

class Main(object):

        def __init__(self):
		screenSize = (640,480)
                surface = pygame.display.set_mode(screenSize)

                green = (0,255,0)
                
                myBox = Box()

                myBox2 = Box()
                myBox2.color = (255,0,0)
                myBox2.size = (70,70)
                myBox2.x = 300
                myBox2.y = 100
                
                myBox3 = Box()
                myBox3.color = (0,0,0)
                myBox3.size = (30,30)
                myBox3.x = 500
                myBox3.y = 200

                done = False
	
                while not done:
                        surface.fill(green)#makes the block move instead of cloning it
                        myBox.update()
                        myBox2.update()
                        myBox3.update()
                        
                        myBox.draw(surface)
                        myBox2.draw(surface)
                        myBox3.draw(surface)
		
                        pygame.display.flip()

                        events = pygame.event.get()

                        for e in events:
                                if e.type is QUIT:
                                        done = True

                                elif e.type is KEYDOWN:
                                        if e.key == K_q:
                                                done = True
		
class Box(object):

	def __init__(self):
                self.x = 0
		self.y = 0
		self.vx = 1
		self.vy = 1
        	self.size = (50,50)
        	self.color = (0,0,255)

	def update(self):
                time.sleep(0.01)
		self.x += self.vx
		self.y += self.vy
		
		if self.x > 640:
			self.vx = -1
		
		if self.x < 0:
			self.vx = 1
		
		if self.y > 480:
			self.vy = -1
		
		if self.y < 0:
			self.vy = 1
			
	def draw(self, surface):
                rect = pygame.Rect((self.x, self.y), self.size)
		pygame.draw.ellipse(surface, self.color, rect)
		
Main()
	
	
