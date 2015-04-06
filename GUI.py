import pygame, sys, substringSearch
import pygame.font
from pygame.locals import *
from enum import Enum


class MidiFind():

	def performRecognition(self,contour):
		str(contour).replace('a','u')
		substringSearch.makeDFA(contour)
		print(midiSong.main())


	def __init__(self):
		#Initialize the game
		pygame.init()
		#Initialize our clock
		self.fpsClock = pygame.time.Clock()

		#Create a screen for us to draw on
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

		self.helptext = pygame.sprite.Sprite()

		self.buttons = pygame.sprite.Group()
		self.helpcontent = pygame.sprite.Group()

		self.helppage = 1
		self.buttons.add(self.button1, self.button2, self.button3)
		self.helpcontent.add(self.helptext)

		#Input contour stuff
		self.inputcontour = ""
		self.contourfont = pygame.font.Font("./Assets/Arial.ttf", 42)
		self.contourfont.set_italic(True)
		
		
		self.contoursurf = self.contourfont.render(self.inputcontour, 1, (0,0,0))


	def main(self):
		#Game loop
		while True:
			self.fpsClock.tick(60)

			if self.needsRedraw:
				self.redrawPage(self.menuPage)
				self.needsRedraw = False



			#Cycle through all received events
			for event in pygame.event.get():
				
				#If QUIT is called, exit the app
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				#If the mouse button is pressed up
				if event.type == pygame.MOUSEBUTTONUP:
					#Get the mouse position
					mouse_pos = pygame.mouse.get_pos()

					#BUTTON 1 CLICKED
					if pygame.Rect(self.button1.rect).collidepoint(mouse_pos):
						
						if (self.menuPage == Page.main):
							self.menuPage = Page.recognize
							self.needsRedraw = True


						elif (self.menuPage == Page.recognize):
							#Perform recognition using the input contour
							self.performRecognition(self.inputcontour)
							print("")
						elif (self.menuPage == Page.success):
							print("")
						elif (self.menuPage == Page.failure):
							##Failure
							print("")

					#BUTTON 2 CLICKED
					if pygame.Rect(self.button2.rect).collidepoint(mouse_pos):

						if (self.menuPage == Page.main):
							##Options
							print("")
						elif (self.menuPage == Page.recognize):
							self.menuPage = Page.help
							self.needsRedraw = True

						elif (self.menuPage == Page.success):
							#Back to Main
							self.menuPage = Page.main
							self.needsRedraw = True
						elif (self.menuPage == Page.failure):
							self.menuPage = Page.recognize
							self.needsRedraw = True
						elif (self.menuPage == Page.help):
							if (self.helppage != 3):
								self.helppage += 1
							else:
								self.helppage = 1
								self.menuPage = Page.recognize
							self.needsRedraw = True

					#BUTTON 3 CLICKED

					if pygame.Rect(self.button2.rect).collidepoint(mouse_pos):
						
						if (self.menuPage == Page.main):
							#Exit
							pygame.quit()
							sys.exit()							
						elif (self.menuPage == Page.recognize):
							#Back to Main
							self.menuPage = Page.main
							self.needsRedraw = True
						elif (self.menuPage == Page.success):
							#Exit
							pygame.quit()
							sys.exit()	
						elif (self.menuPage == Page.failure):
							#Failure
							print("")

				#Key was pressed down, only check it if we're on Page.recognize

				if event.type == pygame.KEYUP and self.menuPage == Page.recognize:
					#A 
					if (event.key == 97):
						self.inputcontour = self.inputcontour + "A"
					#S
					if (event.key == 115):
						self.inputcontour = self.inputcontour + "S"	
					#D
					if (event.key == 100):
						self.inputcontour = self.inputcontour + "D"
					#Backspace
					if (event.key == 8):
						self.inputcontour = self.inputcontour[:-1]

					print(event.key)

					self.needsRedraw = True

					#97 = A
					#115 = S
					#100 = D


			pygame.display.update()

	def redrawPage(self,page):
		#Switch/case doesn't exist in Python so instead we'll use if / elif
		
		print("Redrawing page")

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

		elif page == Page.success:

			backImage = pygame.image.load('./assets/success.png')

			self.button1img = pygame.image.load('./assets/done.png')
			self.button2img = pygame.image.load('./assets/nexttrack.png')
			self.button3img = pygame.image.load('./assets/exit.png')

		elif page == Page.failure:

			backImage = pygame.image.load('./assets/failure.png')

			self.button1img = pygame.image.load('./assets/none.png')
			self.button2img = pygame.image.load('./assets/startover.png')
			self.button3img = pygame.image.load('./assets/none.png')
		
		elif page == Page.help:

			backImage = pygame.image.load('./assets/helpback.png')

			self.button1img = pygame.image.load('./assets/none.png')
			self.button2img = pygame.image.load('./assets/next.png')
			self.button3img = pygame.image.load('./assets/back.png')

			if (self.helppage == 3):
				self.button2img = pygame.image.load('./assets/doneblue.png')


			self.helptext.image = pygame.image.load('./assets/helptext'+str(self.helppage)+'.png')
			print('./assets/helptext'+str(self.helppage)+'.png')
			self.helptext.rect = [1024/2 - self.helptext.image.get_width()/2, 238, self.helptext.image.get_width(), self.helptext.image.get_height()]



		#Blit the background onto our screen
		self.screen.blit(backImage, (0,0))
		#Set the image and rect for each of our buttons
		if (self.button1img != None):
			self.button1.image = self.button1img
			self.button1.rect = [1024/2 - self.button1img.get_width()/2, 522, self.button1img.get_width(), self.button1img.get_height()]
		if (self.button2img != None):
			self.button2.image = self.button2img
			self.button2.rect = [1024/2 - self.button2img.get_width()/2, 588, self.button2img.get_width(), self.button2img.get_height()]
		if (self.button3img != None):
			self.button3.image = self.button3img
			self.button3.rect = [1024/2 - self.button3img.get_width()/2, 655, self.button3img.get_width(), self.button3img.get_height()]

		#Draw the help text if we're on the help screen

		if (page == Page.help):
			self.helpcontent.draw(self.screen)


		#Draw the input contour if we're on the Recognition screen

		if (page == Page.recognize):
			#Create a surface for the inputted contour
			self.contoursurf = self.contourfont.render(self.inputcontour, 1, ((114,114,114)))
			#Blit the surface to the screen
			self.screen.blit(self.contoursurf, (1024/2 - self.contoursurf.get_width()/2 + 12,335))

		#Draw our buttons
		self.buttons.draw(self.screen)
		


		#Flip the display
		pygame.display.flip()



class Page(Enum):
	main = 1
	recognize = 2
	options = 3
	success = 4
	failure = 5
	help = 6


midiFind = MidiFind()
MidiFind.main(midiFind)