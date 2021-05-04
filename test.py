import pygame

done = 0

pygame.init()

screen = pygame.display.set_mode((450,800))
clock = pygame.time.Clock()

bg = pygame.image.load('bg.png')

pygame.display.set_caption('Mobile Phone Emulator')

while done != 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = 1
			break
		if event.type == pygame.MOUSEMOTION:
			print("Yay")
			break

	screen.fill((118,130,121))
	screen.blit(bg, (0, 0))

	pygame.display.flip()
	clock.tick(75)
