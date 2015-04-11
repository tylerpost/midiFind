import pygame, sys, quicksort, midiSong, stringSort

import pygame.font
from pygame.locals import *
from enum import Enum


class MidiFind():

	#Uses the midiSong module to find and return a set of songs matching contour
	def performRecognition(self,contour):
		contour = contour.replace('A','u').replace('S','r').replace('D','d')
		songs = midiSong.findSong(contour) 
		if songs == None:
			return songs
		elif (len(songs) == 50):
			self.failuretype = True
			return None
		else:
			print(len(songs))
			if (self.sorttype == "occ"):
				quicksort.quicksort(songs)
				songs.reverse()
			else:
				stringSort.stringSort(songs, self.sorttype)
			return songs

	#Sorts the songs using either artist or title sort
	def sortSongs(songs, by):

		stringsort.stringSort(songs, by)
		return songs


	#Uses pygame's midi library to play the midi file associated with the passed Song object
	def playSong(self, song):
		songPath = "./" + song.fileLocation.replace('\\', '/')

		freq = 44100    # audio CD quality
		bitsize = -16   # unsigned 16 bit
		channels = 2    # 1 is mono, 2 is stereo
		buffer = 1024    # number of samples
		#Initiate the music module with some standard settings
		pygame.mixer.init(freq, bitsize, channels, buffer)

		try:
			pygame.mixer.music.load(songPath)
			print ("Music file %s loaded!" % songPath)
			pygame.mixer.music.play()
		except:
			print ("File not found!" + songPath)
        		



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
		self.menupage = Page.main

		#Set a boolean to determine if we need a redraw
		self.needsredraw = True

		self.button1 = pygame.sprite.Sprite()
		self.button2 = pygame.sprite.Sprite()
		self.button3 = pygame.sprite.Sprite()
		self.button4 = pygame.sprite.Sprite()

		self.helptext = pygame.sprite.Sprite()

		self.buttons = pygame.sprite.Group()
		self.helpcontent = pygame.sprite.Group()

		self.helppage = 1
		self.buttons.add(self.button1, self.button2, self.button3, self.button4)
		self.helpcontent.add(self.helptext)

		#Input contour stuff
		self.inputcontour = ""
		self.contourfont = pygame.font.Font("./Assets/Arial.ttf", 42)
		self.contourfont.set_italic(True)
		self.sorttype = "occ"
		
		#Results stuff
		self.results = None
		self.resultsindex = 0
		self.resultsfont = pygame.font.Font("./Assets/Arial.ttf", 42)

		#Failure stuff
		self.failuretype = False

	def main(self):
		#Game loop
		while True:
			self.fpsClock.tick(60)

			if self.needsredraw:
				self.redrawPage(self.menupage)
				self.needsredraw = False



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
						
						if (self.menupage == Page.main):
							self.menupage = Page.recognize
							self.inputcontour = ""
							self.needsredraw = True


						elif (self.menupage == Page.recognize):
							#Perform recognition using the input contour
							#Results are saved in an Artist array 
							if (len(self.inputcontour) > 0):
								self.results = self.performRecognition(self.inputcontour)
								#Check if the results isn't None, if it isnt, we found a match
								if (self.results != None):
									self.resultsindex = 0
									self.menupage = Page.success
								#Otherwise the search failed
								else:
									self.inputcontour = ""
									self.menupage = Page.failure
								self.needsredraw = True
						elif (self.menupage == Page.success):
							#Back to Main
							pygame.mixer.music.stop()
							self.menupage = Page.main
							self.needsredraw = True
						elif (self.menupage == Page.failure):
							##Failure
							print("Failure")

					#BUTTON 2 CLICKED
					if pygame.Rect(self.button2.rect).collidepoint(mouse_pos):

						if (self.menupage == Page.main):
							##Options
							print("")
						elif (self.menupage == Page.recognize):
							self.menupage = Page.help
							self.needsredraw = True

						elif (self.menupage == Page.success and self.resultsindex < len(self.results) - 1):
							print("Next")
							#Stop the music
							pygame.mixer.music.stop()
							#Next was pressed, so increment the resultsindex
							self.resultsindex += 1
							self.menupage = Page.success
							self.needsredraw = True
						elif (self.menupage == Page.failure):
							self.menupage = Page.recognize
							self.needsredraw = True
						elif (self.menupage == Page.help):
							if (self.helppage != 3):
								self.helppage += 1
							else:
								self.helppage = 1
								self.menupage = Page.recognize
							self.needsredraw = True

					#BUTTON 3 CLICKED

					if pygame.Rect(self.button3.rect).collidepoint(mouse_pos):
						
						if (self.menupage == Page.main):
							#Exit
							pygame.quit()
							sys.exit()							
						elif (self.menupage == Page.recognize):
							#Back to Main
							self.menupage = Page.main
							self.needsredraw = True
						elif (self.menupage == Page.success):
							#Exit
							pygame.quit()
							sys.exit()	
						elif (self.menupage == Page.failure):
							#Failure
							print("")
						elif (self.menupage == Page.help):
							if (self.helppage != 1):
								self.helppage -= 1
							self.needsredraw = True


					#BUTTON 4 CLICKED		
					if pygame.Rect(self.button4.rect).collidepoint(mouse_pos):
						#Cycle through the sort types
						if (self.menupage == Page.recognize):
							if (self.sorttype == "artist"):
								self.sorttype = "name"
							elif (self.sorttype == "name"):
								self.sorttype = "occ"
							elif (self.sorttype == "occ"):
								self.sorttype = "artist"
							self.needsredraw = True

				#Key was pressed down, only check it if we're on Page.recognize

				if event.type == pygame.KEYUP and self.menupage == Page.recognize:
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

					self.needsredraw = True

					#97 = A
					#115 = S
					#100 = D

				if event.type == pygame.KEYUP and  event.key == K_SPACE and self.menupage == Page.success:
					#Stop the music if space is pressed
					pygame.mixer.music.stop()


			#pygame.display.update()

	def redrawPage(self,page):
		#Switch/case doesn't exist in Python so instead we'll use if / elif
		
		print("Redrawing page")

		#Main
		if page == Page.main:
			#Set the background for our main page
			backimage = pygame.image.load('./assets/main.png')
			#Set our buttons
			self.button1img = pygame.image.load('./assets/beginrecognition.png')
			self.button2img = pygame.image.load('./assets/none.png')
			self.button3img = pygame.image.load('./assets/exit.png')
			self.button4img = pygame.image.load('./assets/none.png')


		elif page == Page.recognize:
			#Set the background for our recognize page
			backimage = pygame.image.load('./assets/recognition.png')
			#Set the buttons
			self.button1img = pygame.image.load('./assets/recognize.png')
			self.button2img = pygame.image.load('./assets/help.png')
			self.button3img = pygame.image.load('./assets/back.png')
			self.button4img = pygame.image.load('./assets/none.png')
			#Set sort by button image depending on the current sorttype
			if (self.sorttype == "artist"):
				self.button4img = pygame.image.load('./assets/sortartist.png')
			elif (self.sorttype == "name"):
				self.button4img = pygame.image.load('./assets/sortsong.png')
			elif (self.sorttype == "occ"):
				self.button4img = pygame.image.load('./assets/sortrelev.png')

		elif page == Page.success:

			backimage = pygame.image.load('./assets/success.png')
			#If we still have guesses to go, set button1 to be blank and button2 to be Next
			if (self.resultsindex == len(self.results)-1):
				print(len(self.results))
				self.button1img = pygame.image.load('./assets/done.png')
				self.button2img = pygame.image.load('./assets/none.png')

			else:
			#If we're on the last guess, set button1 to be Done and button2 to be blank
				self.button1img = pygame.image.load('./assets/none.png')
				self.button2img = pygame.image.load('./assets/nextguess.png')
			self.button3img = pygame.image.load('./assets/exit.png')
			self.button4img = pygame.image.load('./assets/none.png')


		elif page == Page.failure:
			if self.failuretype == False:
				backimage = pygame.image.load('./assets/failure.png')
			else:
				backimage = pygame.image.load('./assets/failureinput.png')

			self.button1img = pygame.image.load('./assets/none.png')
			self.button2img = pygame.image.load('./assets/startover.png')
			self.button3img = pygame.image.load('./assets/none.png')
			self.button4img = pygame.image.load('./assets/none.png')

		
		elif page == Page.help:

			backimage = pygame.image.load('./assets/helpback.png')

			self.button1img = pygame.image.load('./assets/none.png')
			self.button2img = pygame.image.load('./assets/next.png')
			self.button3img = pygame.image.load('./assets/back.png')
			self.button4img = pygame.image.load('./assets/none.png')
			#If we are on the last page, display the done button
			if (self.helppage == 3):
				self.button2img = pygame.image.load('./assets/doneblue.png')
			#If we are on the first page, don't display a back button
			if (self.helppage == 1):
				self.button3img = pygame.image.load('./assets/none.png')
			#Set the helptext image based on the currently selected helppage
			self.helptext.image = pygame.image.load('./assets/helptext'+str(self.helppage)+'.png')
			#Set a positino for the helptext
			self.helptext.rect = [1024/2 - self.helptext.image.get_width()/2, 238, self.helptext.image.get_width(), self.helptext.image.get_height()]



		#Blit the background onto our screen
		self.screen.blit(backimage, (0,0))
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
		if (self.button4img != None):
			self.button4.image = self.button4img
			self.button4.rect = [1024/2 - self.button4img.get_width()/2, 466, self.button4img.get_width(), self.button4img.get_height()]




		#Draw the help text if we're on the help screen

		if (page == Page.help):
			self.helpcontent.draw(self.screen)

		#Draw the results content if we're on the success screen

		if (page == Page.success):
			#Create a string for the artist / song to display
			song = self.results[self.resultsindex]
			songstring = song.name + " - " + song.artist
			#Create a surface for the results text
			self.resultssurf = self.resultsfont.render(songstring, 1, ((114,114,114)))
			self.screen.blit(self.resultssurf, (1024/2 - self.resultssurf.get_width()/2, 335))

			#Let's play the song that we found!
			self.playSong(song)

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
