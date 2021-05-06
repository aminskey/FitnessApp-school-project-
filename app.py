import pygame
import playsound

from gtts import gTTS
from tempfile import TemporaryFile
from pygame.locals import *
from random import randrange, randint
from os import remove

done = 0

pygame.init()

screen = pygame.display.set_mode((450,800))
clock = pygame.time.Clock()

bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, (screen.get_width(), screen.get_height()))


run = pygame.image.load('run.png')
walk = pygame.image.load('walking.png')
eat = pygame.image.load('eating.png')
cycle = pygame.image.load('cycle.png')
weight = pygame.image.load('weight.png')
logger = pygame.image.load('logger.png')
house = pygame.image.load('back.png')

calburn = pygame.image.load('badges/calorieburner.png')
calburn = pygame.transform.scale(calburn, (55, 110))

pygame.display.set_caption('Mobile Phone Emulator')

RED = (209, 9, 79)
GREEN = (30, 94, 10)

win = False


def speech(string, Lang='en'):

	tts = gTTS(string, lang=Lang)
	tts.save('file.mp3')
	playsound.playsound('file.mp3')
	remove('file.mp3')


def setupScreen():

	screen.blit(bg, (0, 0))

	# apps
	screen.blit(run, (40, 260))
	screen.blit(walk, (screen.get_width() * 3/4, 320))
	screen.blit(eat, (screen.get_width() * 3/16, 120))
	screen.blit(cycle, (screen.get_width() * 5/8, 170))
	screen.blit(weight, (screen.get_width() * 11/32, 400))
	screen.blit(logger, (screen.get_width() * 1/2, screen.get_height() * 3/8))

def runScreen():

	background = pygame.image.load('runbg.png')
	background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

	screen.blit(background, (0, 0))

	w = screen.get_width() * 6//8
	l = screen.get_height() * 6//8

	l2 = screen.get_height() * 3//8

	s = pygame.Surface((w, l))
	stats = pygame.Surface((w, l2))
	graph = pygame.Surface((w * 6//8, l2 * 5//8))

	# Opacity
	s.set_alpha(200)
	stats.set_alpha(200)
	graph.set_alpha(50)

	# Color
	s.fill((20,20,20))
	stats.fill((255,255,255))
	graph.fill((255,255,255))

	# width and height
	sw, sh = stats.get_size()

	# Graph
	pygame.draw.line(stats, (0,0,0), (sw * 1//8, sh * 1//8), (sw * 1//8, sh * 7//8))
	pygame.draw.line(stats, (0,0,0), (sw * 1//16, sh * 6//8), (sw * 7//8, sh * 6//8))


	pygame.draw.line(graph, RED, (0, -1 * 0 + graph.get_height() * 1), (20, -1 * 10 + graph.get_height()*1), 5)
	pygame.draw.line(graph, RED, (20, -1 * 10 + graph.get_height() * 1), (60, -1 * 40 + graph.get_height() * 1), 5)
	pygame.draw.line(graph, RED, (60, -1 * 40 + graph.get_height() * 1), (200, -1 * 80 + graph.get_height() * 1), 5)
	pygame.draw.line(graph, RED, (200, -1 * 80 + graph.get_height() * 1), (graph.get_width() * 2, -1 * graph.get_height() * 1), 5)

	# Sending Data to screen
	screen.blit(s, (screen.get_width() * 1//8, screen.get_height() * 1//8))
	screen.blit(stats, (screen.get_width() * 1//8, screen.get_height() * 2//8))
	screen.blit(graph, (screen.get_width() * 7//32, screen.get_height() * 19//64))


	# Text stuff
	kmtagpos = (stats.get_width() * 1//2, sh * 12//8)
	timetagpos = (sw * 1//4, sh * 11//16)

	font = pygame.font.SysFont(None, 50)
	font2 = pygame.font.SysFont(None, 30)
	font3 = pygame.font.SysFont(None, 180)
	font4 = pygame.font.SysFont(None, 120)


	text = font.render('Kilometer', True, RED)
	text2 = font.render('løbet', True, RED)

	cals1 = font.render('Kalorier', True, RED)
	cals2 = font.render('Brændt', True, RED)

	km = font3.render('19', True, RED)
	res = font4.render(str((60*19)/1000) + 'K', True, RED)

	kmtag = font2.render('Kilometer', True, (0, 0, 0))
	timetag = font2.render('Tid', True, (0, 0, 0))


	screen.blit(text, (screen.get_width() * 1//8, screen.get_height() * 1//8))
	screen.blit(text2, (screen.get_width() * 1//8, screen.get_height() * 3//16)+(1,1))
	screen.blit(km, (screen.get_width() * 9//16, screen.get_height() * 1//8 - 10))

	screen.blit(cals1, (screen.get_width() * 1//8, screen.get_height() * 21//32))
	screen.blit(cals2, (screen.get_width() * 1//8, screen.get_height() * 23//32))
	screen.blit(res, (screen.get_width() * 7//16, screen.get_height() * 21//32))


	screen.blit(calburn, (screen.get_width() * 10//16, screen.get_height() * 3//4))

	screen.blit(kmtag, kmtagpos)
	screen.blit(timetag, timetagpos)

	win = True

	log = (19, 60*90)

	return win

def foodScreen():
	background = pygame.image.load('foodbackground.png')
	background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

	screen.blit(background, (0,0))

	w = screen.get_width() * 6//8
	l = screen.get_height() * 6//8

	font1 = pygame.font.SysFont(None, 40)
	font2 = pygame.font.SysFont(None, 20)

	monday = font1.render('Monday', True, (0,0,0))
	tuesday = font1.render('Tuesday', True, (0,0,0))
	wednsday = font1.render('Wednsday', True, (0,0,0))

	mondayTxt = font2.render('I dag skal du have spist salat og Brød:', True, GREEN)
	mondayTxt2 = font2.render('Russisk salat, Israelske Salat osv (Husk komplekse kulhydrater)', True, GREEN)

	tuesdayTxt = font2.render('Spise salat, med diverse frugter og sandwich', True, GREEN)
	tuesdayTxt2 = font2.render('Måske: Granatæble, kylling sandwich, andre slags frugt', True, GREEN)


	wednsdayTxt = font2.render('Cheat Day!! (Denne dag kommer hver 8. måned)', True, GREEN)
	wednsdayTxt2 = font2.render('Spis Hvad du har lyst til', True, GREEN)


	stats = pygame.Surface((w, l))
	stats.set_alpha(200)
	stats.fill((230, 230, 230))

	# Monday
	pygame.draw.line(stats, (0, 0, 0), (stats.get_width() * 1//8, stats.get_height() * 1//8), (stats.get_width()*7//8, stats.get_height() * 1//8), 5)
	pygame.draw.line(stats, (0, 0, 0), (stats.get_width() * 1//8, stats.get_height() * 2//8), (stats.get_width()*7//8, stats.get_height() * 2//8), 5)

	# Tuesday
	pygame.draw.line(stats, (0, 0, 0), (stats.get_width() * 1//8, stats.get_height() * 4//8), (stats.get_width()*7//8, stats.get_height() * 4//8), 5)
	pygame.draw.line(stats, (0, 0, 0), (stats.get_width() * 1//8, stats.get_height() * 5//8), (stats.get_width()*7//8, stats.get_height() * 5//8), 5)

	# Wednsday
	pygame.draw.line(stats, (0, 0, 0), (stats.get_width() * 1//8, stats.get_height() * 7//8), (stats.get_width()*7//8, stats.get_height() * 7//8), 5)
	pygame.draw.line(stats, (0, 0, 0), (stats.get_width() * 1//8, stats.get_height() * 8//8), (stats.get_width()*7//8, stats.get_height() * 8//8), 5)

	screen.blit(stats, (screen.get_width() * 1//8, screen.get_height() * 1//8))

	screen.blit(monday, ((stats.get_width() - len('Monday'))/2, 4 * stats.get_height() * 1//16))
	screen.blit(tuesday, ((stats.get_width() - len('Tuesday'))/2, 4 * stats.get_height() * 5//32))
	screen.blit(wednsday, ((stats.get_width() - len('Wednsnday'))/2, 4 * stats.get_height() * 8//32))

	screen.blit(mondayTxt, (stats.get_width() * 3//16, 4 * stats.get_height() * 5//64))
	screen.blit(mondayTxt2, (stats.get_width() * 3//16, 4 * stats.get_height() * 3//32))

	screen.blit(tuesdayTxt, (stats.get_width() * 3//16, 4 * stats.get_height() * 11//64))
	screen.blit(tuesdayTxt2, (stats.get_width() * 3//16, 4 * stats.get_height() * 6//32))

	screen.blit(wednsdayTxt, (stats.get_width() * 3//16, 4 * stats.get_height() * 17//64))
	screen.blit(wednsdayTxt2, (stats.get_width() * 3//16, 4 * stats.get_height() * 9//32))

def trainingScreen():
	background = pygame.image.load('trainbackground.png')
	background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

	screen.blit(background, (0, 0))

def cycleScreen():
	background = pygame.image.load('cycleBackground.png')
	background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

	screen.blit(background, (0, 0))

def walkScreen():
	background = pygame.image.load('walkBackground.png')
	background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

	screen.blit(background, (0, 0))

def loggerScreen():
	background = pygame.image.load('lgbg.png')
	background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

	w = screen.get_width() * 6//8
	l = screen.get_height() * 6//8

	stats = pygame.Surface((w, l))
	data = pygame.Surface((w, l * 3//8))


	stats.set_alpha(200)
	data.set_alpha(200)

	stats.fill((50, 50, 50))
	data.fill((230, 230, 230))


	screen.blit(background, (0, 0))
	screen.blit(stats, (screen.get_width() * 1//8, screen.get_height() * 1//8))
	screen.blit(data, (screen.get_width() * 1//8, screen.get_height() * 2//8))


def hitBox(image, mpos, startpos):
	x2, y2 = image.get_size()
	mx, my = mpos
	x1, y1 = startpos

	x2 = x1 + x2
	y2 = y1 + y2

	if (mx > x1 and mx < x2) and (my > y1 and my < y2):
		return True
	else:
		return False

setState = 1

while done != 1:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = 1
			break
		else:
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				print(hitBox(run, pos, (40, 260)))

				if setState == 1:
					if hitBox(run, pos, (40, 260)):
						setState = 0
						win=runScreen()

					elif hitBox(eat, pos, (screen.get_width() * 3/16, 120)):
						setState = 0
						foodScreen()

					elif hitBox(weight, pos, (screen.get_width() * 11/32, 400)):
						setState = 0
						trainingScreen()

					elif hitBox(cycle, pos, (screen.get_width() * 5/8, 170)):
						setState = 0
						cycleScreen()

					elif hitBox(walk, pos, (screen.get_width() * 3/4, 320)):
						setState = 0
						walkScreen()

					elif hitBox(logger, pos, (screen.get_width() * 1/2, screen.get_height() * 3/8)):
						setState = 0
						loggerScreen()

				elif setState == 0:
					if hitBox(house, pos, (0, 0)):
						setState = 1
	if setState == 1:
		setupScreen()
	else:
		house = pygame.transform.scale(house, (100, 100))
		screen.blit(house, (0,0))


	# screen background color


	pygame.display.update()
	clock.tick(75)

pygame.display.quit()
