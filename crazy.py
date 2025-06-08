#3:10:00
import pygame
from sys import exit
from settings import config
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        playerWalk1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
        playerWalk2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
        self.playerWalk = [playerWalk1, playerWalk2]
        self.playerIndex = 0
        self.playerJump = pygame.image.load("graphics/player/jump.png").convert_alpha()

        self.image = self.playerWalk[self.playerIndex] 
        self.rect = self.image.get_rect(midbottom = (200,300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
    def apply_gravity(self):
        self.gravity +=1 
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    def animation(self):
        if self.rect.bottom < 300:
            self.image = self.playerJump
        else:
            self.playerIndex += 0.1
            if self.playerIndex >= len(self.playerWalk):
                self.playerIndex = 0
            self.image = self.playerWalk[int(self.playerIndex)]
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'fly':
            flyFrame1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
            flyFrame2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
            self.frames = [flyFrame1, flyFrame2]
            y_pos = 210
        else:
            snailFrame1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snailFrame2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames = [snailFrame1, snailFrame2]
            y_pos = 300
        self.animationIndex = 0
        self.image = self.frames[self.animationIndex]
        self.rect = self.image.get_rect(midbottom=(randint(900,1100), y_pos))

    def animation(self):
        self.amination += 0.1
        if self.animationIndex >= len(self.frames):
            self.animationIndex = 0
        self.image = self.frames[int(self.animationIndex)]
    def update(self):
        self.animation()
        self.rect.x -= 6




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
player = pygame.sprite.GroupSingle()
player.add(Player())

obsstacleGroup = pygame.sprite.Group()

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
            obsstacleGroup.add(Obstacle('fly'))
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
        
#PLAYER....PLAYER 
        playerGravity += 1
        playerRectangle.y += playerGravity 
        if playerRectangle.bottom >= 300: 
            playerRectangle.bottom = 300 
        playerAnimation()
        screen.blit(playerSurface, playerRectangle)
        player.draw(screen)
        player.update()
        obsstacleGroup.draw(screen)
        obsstacleGroup.update()

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
 
    