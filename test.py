import pygame

done = 0

pygame.init()

screen = pygame.display.set_mode((450,800))
clock = pygame.time.Clock()

bg = pygame.image.load('bg.png')

run = pygame.image.load('run.png')
walk = pygame.image.load('walking.png')
eat = pygame.image.load('eating.png')
cycle = pygame.image.load('cycle.png')
weight = pygame.image.load('weight.png')
logger = pygame.image.load('logger.png')


pygame.display.set_caption('Mobile Phone Emulator')


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


	# screen background image
	screen.blit(bg, (0, 0))

	# apps
	screen.blit(run, (40, 260))
	screen.blit(walk, (400 * 3/4, 320))
	screen.blit(eat, (400 * 3/16, 120))
	screen.blit(cycle, (400 * 5/8, 170))
	screen.blit(weight, (400 * 11/32, 400))
	screen.blit(logger, (400 * 1/2, 800 * 3/8))


	pygame.display.update()
	clock.tick(75)
