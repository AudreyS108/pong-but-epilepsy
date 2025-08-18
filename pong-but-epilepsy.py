#PLAN:
#1. Have main pong game which is functional
#2. Add epilepsy effect by flashing the screen with random rgb colors
#3. Add a "First to ___ points wins" system + game over screen declaring the winner.
#4. Create a main menu to start game
#5. Add Epilepsy and non epilepsy modes (incl epilepsy warning)
#6. Possibly add a "How to play" screen
#7. Possibly add a pong bot with AI - single player
#6. Optional: Add sound effects and music
#Thats it for now


import pygame
import sys
import random

pygame.init()
# Setting up screen dimensions
width, height = 1280, 720

screen = pygame.display.set_mode((width, height))
screen.fill("black")
pygame.display.set_caption("Pong but epilepsy")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 30)

# da paddles
playerone = pygame.Rect(110, (height/2) - 50, 10, 100)
playertwo = pygame.Rect(width - 110, (height/2) - 50, 10, 100)

#Player scores
p1score = 0
p2score = 0

ball = pygame.Rect((width/2) - 10, (height/2) - 10, 20, 20)
xspeed, yspeed = random.choice([-1, 1]), random.choice([-2, -1, 1, 2])

#Pygame loop
while True:
    # --------Quit Pygame window--------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #--- end pygame window quit

    # --------Paddle movement!----------
    
    keyspressed = pygame.key.get_pressed()

    # Player One controls
    if keyspressed[pygame.K_w]:
        if playerone.bottom < height:
            playerone.top += 2 # Flipped controls contrary to real world logistics: designed to be extra confusing
    elif keyspressed[pygame.K_s]:
        if playerone.top > 0:
            playerone.bottom -= 2
        
    # Player Two controls
    if keyspressed[pygame.K_UP]:
        if playertwo.bottom < height:
            playertwo.top += 2 
    elif keyspressed[pygame.K_DOWN]:
        if playertwo.top > 0:
            playertwo.bottom -= 2
    
    # --------Ball physics------------
    if ball.y >= height:
        yspeed =  random.choice([-2, -1, 1, 2])
    if ball.y <= 0:
        yspeed =  random.choice([-2, -1, 1, 2])

    if ball.x <= 0: #Left side
        ball.center = width/2, height/2
        xspeed = random.choice([-1, 1])
        yspeed =  random.choice([-2, -1, 1, 2])
        p2score += 1 #update the score
        print("Player 1 score:", p1score, ", Player 2 score:", p2score)

    if ball.x >= width: #right side
        ball.center = width/2, height/2
        xspeed = random.choice([-1, 1])
        yspeed =  random.choice([-2, -1, 1, 2])
        p1score += 1 #update the score
        print("Player 1 score:", p1score, ", Player 2 score:", p2score)
    
    if ball.colliderect(playerone) and ball.x < playerone.right:
        xspeed = 1
    if ball.colliderect(playertwo) and ball.x < playertwo.left:
        xspeed = -1

    ball.x += xspeed * 1.4
    ball.y += yspeed * 1.4

    # ----------SCORES DISPLAY-----------
    scoreboardtext = font.render("Scoreboard", True, "white")
    p1text = font.render(str("Player 1: " + str(p1score)), True, "white")
    p2text = font.render(str("Player 2: " + str(p1score)), True, "white")
    
    scoreboardrect = scoreboardtext.get_rect(center=(width/2, 50))
    p1_rect = p1text.get_rect(center=(width/2 - 200, 80))
    p2_rect = p1text.get_rect(center=(width/2 + 200, 80))

    #------------SCREEN FILLS:-----------
    # Screen must be filled to prevent any weird trails
    # epilepsy mode:
    #screen.fill(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  
    # normal mode
    screen.fill("black")

    # draw the player paddles
    pygame.draw.rect(screen, "white", playerone)
    pygame.draw.rect(screen, "white", playertwo)
    pygame.draw.circle(screen, "white", ball.center, 10)

    screen.blit(p1text, p1_rect)
    screen.blit(p2text, p2_rect)
    screen.blit(scoreboardtext, scoreboardrect)

    pygame.display.update()
    # clock.tick : Frames per second
    clock.tick(250)

    