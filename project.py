import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen 
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("31633.jpg")

# Background sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("base.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 7

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("ufo.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.4)
    enemyY_change.append(10)

# Bullet 
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font("freesansbold.ttf", 64)

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 0, 0))
    screen.blit(score, (x, y))

def game_over_text(X):
    over_text = over_font.render("GAME OVER", X, (255, 0, 0))
    screen.blit(over_text, (200, 250))

def player(x,y):
    # Blit means to draw
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    # Blit means to draw
    screen.blit(enemyImg[i], (x, y))

def  fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 21, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True

def main():
    global playerX, playerX_change, bulletX, bulletY, bullet_state, score_value
    # Game Loop
    running = True
    while running:

        screen.fill((0, 0, 0))

        # Background image
        screen.blit(background, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # If keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change -= 0.7
                if event.key == pygame.K_RIGHT:
                    playerX_change += 0.7
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound("laser.wav")
                        bullet_sound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # check for boundaries so it doesnt go out of pass
        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 728:
            playerX = 728

        for i in range(num_of_enemies):

            # Game Over
            if enemyY[i] > 420:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text(True)
            
            # To play again
            if enemyY[i] >= 2000:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            for h in range(num_of_enemies):
                                enemyY[h] = random.randint(50, 150)
                            game_over_text(False)
                            score_value = 0

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 0.4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 728:
                enemyX_change[i] -= 0.4
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosion_sound = mixer.Sound("explosion.wav")
                explosion_sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 735)
                enemyY[i] = random.randint(50, 150)
            
            enemy(enemyX[i], enemyY[i], i)


        # Bullet Movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change
        
        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update() 


if __name__ == "__main__":
    main()