import pygame, sys

from pygame.locals import *
from enum import Enum


class MidiFind():
	def __init__(self):
		#Initialize the game
		pygame.init()
		#Initialize our clock
		self.fpsClock = pygame.time.Clock()

		#Create a screen for us to draw on
		# global screen
		self.screen = pygame.display.set_mode((1024, 768))
		#Give us a caption
		pygame.display.set_caption("MidiFind")

		#Set our enum for the current menu page
		self.menuPage = Page.main

		#Set a boolean to determine if we need a redraw
		self.needsRedraw = True

		self.button1 = pygame.sprite.Sprite()
		self.button2 = pygame.sprite.Sprite()
		self.button3 = pygame.sprite.Sprite()

		self.buttons = pygame.sprite.Group()
		self.buttons.add(self.button1, self.button2, self.button3)


	def main(self):
		#Game loop
		while True:
			self.fpsClock.tick(60)

			if self.needsRedraw:
				self.redrawPage(self.menuPage)
				self.needsRedraw = False




			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.MOUSEBUTTONUP:
					mouse_pos = pygame.mouse.get_pos()
					print(mouse_pos)
					if pygame.Rect(self.button1.rect).collidepoint(mouse_pos):
						print("ayy")
						self.menuPage = Page.recognize
						self.needsRedraw = True;
					if pygame.Rect(self.button2.rect).collidepoint(mouse_pos):
						print("Button 2")
					if pygame.Rect(self.button3.rect).collidepoint(mouse_pos):
						print("Button 3")

			pygame.display.update()

	def redrawPage(self,page):
		#Switch/case doesn't exist in Python so instead we'll use if / elif
		
		#Main
		if page == Page.main:
			#Set the background for our main page
			backImage = pygame.image.load('./assets/main.png')
			#Set our buttons
			self.button1img = pygame.image.load('./assets/beginrecognition.png')
			self.button2img = pygame.image.load('./assets/options.png')
			self.button3img = pygame.image.load('./assets/exit.png')


		elif page == Page.recognize:
			print("test")
			#Set the background for our recognize page
			backImage = pygame.image.load('./assets/recognition.png')
			#Set the buttons
			self.button1img = pygame.image.load('./assets/recognize.png')
			self.button2img = pygame.image.load('./assets/help.png')
			self.button3img = pygame.image.load('./assets/cancel.png')




		#Blit the background onto our screen
		self.screen.blit(backImage, (0,0))
		#Set the image and rect for each of our buttons
		self.button1.image = self.button1img
		self.button1.rect = [1024/2 - self.button1img.get_width()/2, 522, self.button1img.get_width(), self.button1img.get_height()]

		self.button2.image = self.button2img
		self.button2.rect = [1024/2 - self.button2img.get_width()/2, 588, self.button2img.get_width(), self.button2img.get_height()]

		self.button3.image = self.button3img
		self.button3.rect = [1024/2 - self.button3img.get_width()/2, 655, self.button3img.get_width(), self.button3img.get_height()]

		self.buttons.draw(self.screen)

		#Flip the display
		pygame.display.flip()



class Page(Enum):
	main = 1
	recognize = 2
	options = 3
	success = 4
	failure = 5


midiFind = MidiFind()
MidiFind.main(midiFind)