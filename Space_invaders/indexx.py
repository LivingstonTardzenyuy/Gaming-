import pygame

pygame.init()  # we initialize the pygame for our game to work

width = 800
height = 600
screen = pygame.display.set_mode((width, height))  # creating a python screen

# title and icon section
pygame.display.set_caption("Space invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# player image
playImg = pygame.image.load('spaceship.png')
playX = 370
playY = 520


def player():
    screen.blit(playImg, (playX,
                          playY))  # help to draw images in the screen. It has 2 coordintates the playImg and the posion of the player and call it in the while loop


# color
red = 20
green = 30
blue = 150

# Game loop
running = True
while True:  # to enable our screen to last forever
    screen.fill((red, green, blue))

    for event in pygame.event.get():  # iterating throught all our events. we can have events like mouseup, mousedown, quite etc.

        if event.type == pygame.QUIT:  # checking if the event is a quite event
            running = False

        # else:

    player()

    pygame.display.update()  # to make sure all our implimetation is being updated