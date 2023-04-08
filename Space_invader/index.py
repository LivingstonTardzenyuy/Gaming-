import pygame
import random
import math

pygame.init()                   #we initialize the pygame for our game to work

#creating a screen in python
width=800
height=600
screen =pygame.display.set_mode((width, height))             #creating a python screen


#screen picture
background = pygame.image.load('backgrounds.png')


#title and icon section
pygame.display.set_caption("Space invaders")
icon =pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)


#player image
playImg=pygame.image.load('space-invaders.png')
playX = 370
playY = 520
playerX_change=0        
def player(x,y):               #function to draw image in the screen
    screen.blit(playImg, (x, y))           #help to draw images in the screen. It has 2 coordintates the playImg and the posion of the player and call it in the while loop


#enemy position
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

no_of_enemies = 5

for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load('ghosts.png'))
    enemyX.append(random.randint(0, width))
    enemyY.append(random.randint(0, 50))
    enemyX_change.append(2)
    enemyY_change.append(5)


    def enemy(x, y, i):
        screen.blit(enemyImg[i], (x, y))

#color
# red=20
# blue=120

#game over text
font = pygame.font.Font('freesansbold.ttf', 30)
def game_over(x, y):
    over_text = font.render( "GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (400, 300))
    
    
#bullet 
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 520
bulletX_change = 0              #because the bullets won't move in the x direction
bulletY_change = 20
bullet_state = "ready"          #ready state means we cant see bullet on the screen, fire means the bullet is moving......

def firebullet(x, y):
    global bullet_state
    bullet_state = "fire" 
    screen.blit(bulletImg, (x + 16 ,y + 10))         #16 and 10 to allow bullete appear at the cente of our space sheep   


# score
font = pygame.font.Font('freesansbold.ttf', 30)
text_X=5
text_Y=5
score_value =0

def display_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


#function for collision
def is_collision(enemyX, enemyY, bulletX, bulletY):
    x_change = enemyX - bulletX
    y_change = enemyY - bulletY
    distance = math.sqrt((math.pow(x_change, 2))+ (math.pow(y_change, 2)))           #calculating distance between 2 points 
    if distance < 20:
        return True
    else:
        return False
    
#Game loop
running=True
while running:                     #to enable our screen to last forever
    
    # screen.fill((red, green, blue))     #background pic
    
    screen.blit(background, (0, 0))
    
    #bullet image
    
    screen.blit(bulletImg, (0,0))
    
    for event in pygame.event.get():            #iterating throught all our events. we can have events like mouseup, mousedown, quite etc.
        
        if event.type == pygame.QUIT:         #checking if the event is a quite event
            running=False
        
        #keystrock checking if lef or right    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
                # enemyY_change +=enemyY_change
                
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
                # enemyY_change +=enemyY_change
            
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX=playX
                    firebullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                
            # else:
    playX += playerX_change                 #to change the position of the x coordinate
    
    
    #condition so that player should not move out of bounds
    if playX <= 0:
        playX = 0
    elif playX >= 736:
        playX = 736
    
    # print(playX)
    
    for i in range(no_of_enemies):
        
        #game over section
        if enemyY[i] > 500 :
            for j in range(no_of_enemies):
                enemyY = 1500              #so that we dont see any enemy agin
            
            game_over(enemyX, enemyY)
            break 
            
        enemyX[i] +=enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] +=enemyY_change[i]

        elif enemyX[i] >= 736:
            enemyX_change[i] = -3   
            enemyY[i] +=enemyY_change[i]
        
        
        #collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)  
        if collision:                   #if collision occure reset bulletY and the state of bullet
            bulletY = 520
            bullet_state = "ready"
            score_value +=1
            print(score_value)
            enemyImg[i] = pygame.image.load('ghosts.png')
            enemyX[i] = random.randint(0, width)
            enemyY[i] = random.randint(0,30)
        
        enemy(enemyX[i], enemyY[i], i)
    
    # to make sure that when the postion of the bullet is at 0 for y value it should rest to ready and bullet should come back to player
    if bulletY <=0:
        bulletY = 520
        bullet_state = "ready"
        
        
    # bullet movement
    if bullet_state is "fire":
        firebullet(bulletX, bulletY)
        bulletY -=bulletY_change

    player(playX, playY)
    
    display_score(text_X, text_Y)
    
    pygame.display.update()             # to make sure all our implimetation is being updated