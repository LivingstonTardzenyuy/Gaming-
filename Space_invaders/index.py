import pygame
import random
pygame.init()                   #we initialize the pygame for our game to work

width=800
height=600
screen =pygame.display.set_mode((width, height))             #creating a python screen


#screen picture
background = pygame.image.load('background.png')

#title and icon section
pygame.display.set_caption("Space invaders")
icon =pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)


#player image
playImg=pygame.image.load('space-invaders.png')

#current player position
playX = 370
playY = 520
playerX_change=0        



#enemy position
enemyImg = pygame.image.load('enemy.png')
enemyX=random.randint(0, width)
enemyY=random.randint(0, 100)
enemyX_change = 4
enemyY_change = 10


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def player(x,y):               #function to draw image in the screen
    screen.blit(playImg, (x, y))           #help to draw images in the screen. It has 2 coordintates the playImg and the posion of the player and call it in the while loop


#color
red=20
green=130
blue=120

#Game loop
running=True
while running:                     #to enable our screen to last forever
    
    screen.fill((red, green, blue))     #background pic
    
    screen.blit(background, (0, 0))
    

    for event in pygame.event.get():            #iterating throught all our events. we can have events like mouseup, mousedown, quite etc.
        
        if event.type == pygame.QUIT:         #checking if the event is a quite event
            running=False
        
        #keystrock checking if lef or right    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
                
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                
            # else:
    playX += playerX_change                 #to change the position of the x coordinate
    
    
    #condition so that player should not move out of bounds
    if playX <= 0:
        playX = 0
    elif playX >= 800:
        playX = 736
    
    # print(playX)
    
    enemyX +=enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY +=enemyY_change
        
    elif enemyX >= 736:
        enemyX_change = 4    
        enemyY +=enemyY_change
    
    player(playX, playY)
    enemy(enemyX, enemyY)
    
    pygame.display.update()             #to make sure all our implimetation is being updated