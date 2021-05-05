import pygame

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




pygame.display.set_caption('Mobile Phone Emulator')


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

def foodScreen():
	background = pygame.image.load('foodbackground.png')
	background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

	screen.blit(background, (0,0))

def trainingScreen():
	background = pygame.image.load('trainbackground.png')
	background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

	screen.blit(background, (0, 0))

while done != 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = 1
			break
		if event.type == pygame.MOUSEMOTION:
#			print("Yay")
			break

	# screen background color
	screen.fill((118,130,121))


	trainingScreen()

	pygame.display.update()
	clock.tick(75)
