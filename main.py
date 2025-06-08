#3:10:00
import pygame
from sys import exit
from settings import config
from random import randint
def displayScore():
    #global currentTime
    currentTime = int(pygame.time.get_ticks() / 1000) - startTime
    scoreSurface = testFont.render(f"{currentTime}", False, (64,64,64))
    scoreRectangle = scoreSurface.get_rect(center = (400,50))
    screen.blit(scoreSurface, scoreRectangle)
    return currentTime

def obstacleMovement(obstacleList):
    if obstacleList:
        for obstacleRect in obstacleList:
            obstacleRect.x -= 5
            if obstacleRect.bottom == 300:
                screen.blit(snailSurface, obstacleRect)
            else:
                screen.blit(flySurface, obstacleRect)


        obstacleList = [obstacle for obstacle in obstacleList if obstacle.x > -100]

        return obstacleList
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
            for obstacleRectangle in obstacles:
                if player.colliderect(obstacleRectangle):
                    return False
    return True

def playerAnimation():
    global playerSurface, playerIndex

    if playerRectangle.bottom < 300:
        playerSurface = playerJump
    else:
        playerIndex += 0.1 
        if playerIndex >= len(playerWalk):
            playerIndex = 0
        playerSurface = playerWalk[int(playerIndex)]


pygame.init()
screen = pygame.display.set_mode((config["width"], config["height"]))
pygame.display.set_caption("run")
clock = pygame.time.Clock()
testFont = pygame.font.Font("font/Pixeltype.ttf", 50)
gameActive = False
startTime = 0
score = 0

skySurface = pygame.image.load("graphics/sky.png").convert()
gndSurface = pygame.image.load("graphics/ground.png").convert()
#Obstacles


snailFrame1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snailFrame2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snailFrames = [snailFrame1, snailFrame2]
snailFrameIndex = 0
snailSurface = snailFrames[snailFrameIndex]

flyFrame1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
flyFrame2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
flyFrames = [flyFrame1, flyFrame2]
flyFrameIndex = 0
flySurface = flyFrames[flyFrameIndex]

ObstacleRectangleList=[]

playerWalk1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
playerWalk2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
playerWalk = [playerWalk1, playerWalk2]
playerIndex = 0
playerJump = pygame.image.load("graphics/player/jump.png").convert_alpha()
playerSurface = playerWalk[playerIndex] 
playerRectangle = playerSurface.get_rect(midbottom = (80,300))
playerGravity = 0



#Intro Screen
playerStand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
playerStand = pygame.transform.rotozoom(playerStand, 0, 2)
playerStandRectangle = playerStand.get_rect(center = (400, 200))

gameName = testFont.render('Pixel Runner', False, (111,196,169))
gameNameRectangle = gameName.get_rect(center=(400,80))

gameMessage = testFont.render('Press space to run', False, (111,196,169))
gameMessageRectangle = gameMessage.get_rect(center=(400,340))

obstacleTimer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacleTimer, 1500) 

snailAnimationTimer = pygame.USEREVENT + 2
pygame.time.set_timer(snailAnimationTimer, 500)

flyAnimationTimer = pygame.USEREVENT + 3
pygame.time.set_timer(flyAnimationTimer, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if gameActive:
            if event.type == pygame.MOUSEBUTTONDOWN and playerRectangle.bottom  >=300:
                if playerRectangle.collidepoint(event.pos):
                    playerGravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and playerRectangle.bottom  >=300:
                    playerGravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                     gameActive = True
                     startTime = int(pygame.time.get_ticks() / 1000)
        if event.type == obstacleTimer and gameActive:
            if randint(0,2):
                ObstacleRectangleList.append(snailSurface.get_rect(bottomright = (randint(900,1100), 300)))
            else:
                ObstacleRectangleList.append(flySurface.get_rect(bottomright = (randint(900,1100), 210)))
        if event.type == snailAnimationTimer and gameActive:
            if snailFrameIndex == 0:
                snailFrameIndex = 1
            else: snailFrameIndex = 0
            snailSurface = snailFrames[snailFrameIndex]

        if event.type == flyAnimationTimer and gameActive: 
            if flyFrameIndex == 0:
                flyFrameIndex = 1
            else: flyFrameIndex = 0
            flySurface = flyFrames[flyFrameIndex]


 
    if gameActive:
        screen.blit(skySurface, (0,0))
        screen.blit(gndSurface, (0,300))
        score = displayScore()
        
        #PLAYER 
        playerGravity += 1
        playerRectangle.y += playerGravity 
        if playerRectangle.bottom >= 300: 
            playerRectangle.bottom = 300 
        playerAnimation()
        screen.blit(playerSurface, playerRectangle)
        #Obstacle movement
        ObstacleRectangleList = obstacleMovement(ObstacleRectangleList)
        
        gameActive = collisions(playerRectangle, ObstacleRectangleList)
        

    else:
            screen.fill((94,129,162))
            screen.blit(playerStand, playerStandRectangle)
            ObstacleRectangleList.clear()
            playerRectangle.midbottom = (80,300)
            playerGravity = 0
            
            scoreMessage = testFont.render(f"Your score: {score}", False, (111,196,169))
            scoreMessageRectangle = scoreMessage.get_rect(center = (400,330)) 
            screen.blit(gameName, gameNameRectangle)
            if score == 0:
                screen.blit(gameMessage, gameMessageRectangle)
            else:
                screen.blit(scoreMessage, scoreMessageRectangle)

    pygame.display.update()
    clock.tick(60)
 
    