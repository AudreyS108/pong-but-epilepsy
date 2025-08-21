#PLAN:
#1. Have main pong game which is functional {DONE}
#2. Add epilepsy effect by flashing the screen with random rgb colors {DONE}
#3. Add a "First to ___ points wins" system + game over screen declaring the winner. {PARTWAY}
#4. Create a main menu to start game {DONE}
#5. Add Epilepsy and non epilepsy modes {DONE}
#6. Possibly add a "How to play" screen
#7. Possibly add a pong bot with AI - single player
#6. Optional: Add sound effects and music
#8. oPTIonal: add extra bal for epipesy mode
#Thats it for now


import pygame
import sys
import random
from time import sleep

pygame.init()
# Setting up screen dimensions
width, height = 1280, 720

screen = pygame.display.set_mode((width, height))
screen.fill("black")
pygame.display.set_caption("Pong but epilepsy")
clock = pygame.time.Clock()

# da paddles
PlayerOne = pygame.Rect(110, (height/2) - 50, 10, 100)
PlayerTwo = pygame.Rect(width - 110, (height/2) - 50, 10, 100)

#Player scores
p1score = 0
p2score = 0

ball = pygame.Rect((width/2) - 10, (height/2) - 10, 20, 20)
xspeed, yspeed = random.choice([-1, 1]), random.choice([-1, 1])

def MainMenu():
    font = pygame.font.SysFont("Arial", 60)
    fontsmall = pygame.font.SysFont("Arial", 30)

    while True:
        pygame.display.set_caption("Pong but epilepsy - Main Menu")
        screen.fill("black")

        MousePosition = pygame.mouse.get_pos()

        MenuText = font.render("Pong but epilepsy", True, "white")
        MenuRect = MenuText.get_rect(center=(width/2 + 20, 100))

        mx,my = pygame.mouse.get_pos()

        PlayButton = pygame.Rect(width/2 - 100, 200, 250, 75)
        ChaosPlayButton = pygame.Rect(width/2 - 100, 400, 250, 75)
        QuitButton = pygame.Rect(width/2 - 100, 600, 250, 75)


        playbuttontext = fontsmall.render("Play Normal Mode", True, "black")
        chaosbuttontext = fontsmall.render("Play Epilepsy Mode", True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        quitbuttontext = fontsmall.render("Quit Game", True, "black")

        PBrect = playbuttontext.get_rect(center = ((width/2 + 25), 235))
        CBrect = playbuttontext.get_rect(center = ((width/2 + 20), 435))
        QBrect = playbuttontext.get_rect(center = ((width/2 + 60), 635))

        


        if PlayButton.collidepoint(mx, my):
            pygame.draw.rect(screen, "grey", PlayButton)
        else:
            pygame.draw.rect(screen, "white", PlayButton)

        if ChaosPlayButton.collidepoint(mx, my):
            pygame.draw.rect(screen, "grey", ChaosPlayButton)
        else:
            pygame.draw.rect(screen, "white", ChaosPlayButton)

        if QuitButton.collidepoint(mx, my):
            pygame.draw.rect(screen, "grey", QuitButton)
        else:
            pygame.draw.rect(screen, "white", QuitButton)
  
        screen.blit(MenuText, MenuRect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #detects when mouse button is down runs through buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PlayButton.collidepoint(event.pos):
                    play()
                elif ChaosPlayButton.collidepoint(event.pos):
                    chaosplay()
                elif QuitButton.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(playbuttontext, PBrect)
        screen.blit(chaosbuttontext, CBrect)
        screen.blit(quitbuttontext, QBrect)

        pygame.display.update()
        clock.tick(200)

def play():
    font = pygame.font.SysFont("Arial", 30)

    pygame.display.set_caption("Pong but epilepsy - Normal Mode")

# da paddles
    PlayerOne = pygame.Rect(110, (height/2) - 50, 10, 100)
    PlayerTwo = pygame.Rect(width - 110, (height/2) - 50, 10, 100)

#Player scores
    p1score = 0
    p2score = 0

    ball = pygame.Rect((width/2) - 10, (height/2) - 10, 20, 20)
    xspeed, yspeed = random.choice([-1, 1]), random.choice([-1, 1])

    while True:
    
    # --------Quit Pygame window--------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                MainMenu()
    #--- end pygame window quit

    #Winning scores
        if p1score >= 10 or p2score >= 10:
            endscreen()

    # --------Paddle movement!----------

        keyspressed = pygame.key.get_pressed()

    # Player One controls
        if keyspressed[pygame.K_s]:
            if PlayerOne.bottom < height:
                PlayerOne.top += 2 # Flipped controls contrary to real world logistics: designed to be extra confusing
        elif keyspressed[pygame.K_w]:
            if PlayerOne.top > 0:
                PlayerOne.bottom -= 2

    # Player Two controls
        if keyspressed[pygame.K_DOWN]:
            if PlayerTwo.bottom < height:
                PlayerTwo.top += 2 
        elif keyspressed[pygame.K_UP]:
            if PlayerTwo.top > 0:
                PlayerTwo.bottom -= 2
    
    # --------Ball physics------------
        if ball.y >= height:
            yspeed = random.choice([-1, -2])
        if ball.y <= 0:
            yspeed = random.choice([1, 2])

        if ball.x <= 0: #Left side
            ball.center = width/2, height/2
            xspeed = random.choice([-1, 1])
            yspeed =  random.choice([-1, 1])
            p2score += 1 #update the score
            print("Player 1 score:", p1score, ", Player 2 score:", p2score)

        if ball.x >= width: #right side
            ball.center = width/2, height/2
            xspeed = random.choice([-1, 1])
            yspeed =  random.choice([-2, -1, 1, 2])
            p1score += 1 #update the score
            print("Player 1 score:", p1score, ", Player 2 score:", p2score)
    
        if ball.colliderect(PlayerOne) and ball.x < PlayerOne.right:
            xspeed = 1
        if ball.colliderect(PlayerTwo) and ball.x < PlayerTwo.left:
            xspeed = -1

        ball.x += xspeed * 1.4
        ball.y += yspeed * 1.4

    #------------SCREEN FILLS:-----------
    # Screen must be filled to prevent any weird trails
    # normal mode
        screen.fill("black")

    # ----------SCORES DISPLAY-----------
        scoreboardtext = font.render("Scoreboard", True, "white")
        p1text = font.render(str("Player 1: " + str(p1score)), True, "white")
        p2text = font.render(str("Player 2: " + str(p2score)), True, "white")
    
        scoreboardrect = scoreboardtext.get_rect(center=(width/2, 50))
        p1_rect = p1text.get_rect(center=(width/2 - 200, 80))
        p2_rect = p2text.get_rect(center=(width/2 + 200, 80))

        SpaceText = font.render("Press SPACE to return to the main menu", True, "white")
        Spacerect = SpaceText.get_rect(center=(width/2, height - 100))


    # draw the player paddles
        pygame.draw.rect(screen, "white", PlayerOne)
        pygame.draw.rect(screen, "white", PlayerTwo)
        pygame.draw.circle(screen, "white", ball.center, 10)

        screen.blit(p1text, p1_rect)
        screen.blit(p2text, p2_rect)
        screen.blit(scoreboardtext, scoreboardrect)
        screen.blit(SpaceText, Spacerect)

        pygame.display.update()
    # clock.tick : Frames per second
        clock.tick(300)

def chaosplay():
    font = pygame.font.SysFont("Arial", 30)

    pygame.display.set_caption("Pong but epilepsy - Epilepsy Mode")

# da paddles
    PlayerOne = pygame.Rect(110, (height/2) - 50, 10, 100)
    PlayerTwo = pygame.Rect(width - 110, (height/2) - 50, 10, 100)

#Player scores
    p1score = 0
    p2score = 0

    ball = pygame.Rect((width/2) - 10, (height/2) - 10, 20, 20)
    xspeed, yspeed = random.choice([-1, 1]), random.choice([-1, 1])

    while True:
    
    # --------Quit Pygame window--------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                MainMenu()
    #--- end pygame window quit

        if p1score >= 10 or p2score >= 10:
            endscreen()

    # --------Paddle movement!----------

        keyspressed = pygame.key.get_pressed()

    # Player One controls
        if keyspressed[pygame.K_w]:
            if PlayerOne.bottom < height:
                PlayerOne.top += 2 # Flipped controls contrary to real world logistics: designed to be extra confusing
        elif keyspressed[pygame.K_s]:
            if PlayerOne.top > 0:
                PlayerOne.bottom -= 2

    # Player Two controls
        if keyspressed[pygame.K_UP]:
            if PlayerTwo.bottom < height:
                PlayerTwo.top += 2 
        elif keyspressed[pygame.K_DOWN]:
            if PlayerTwo.top > 0:
                PlayerTwo.bottom -= 2
    
    # --------Ball physics------------
        if ball.y >= height:
            yspeed = random.choice([-2, -1])
        if ball.y <= 0:
            yspeed = random.choice([1, 2])

        if ball.x <= 0: #Left side
            ball.center = width/2, height/234
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
    
        if ball.colliderect(PlayerOne) and ball.x < PlayerOne.right:
            xspeed = 1
        if ball.colliderect(PlayerTwo) and ball.x < PlayerTwo.left:
            xspeed = -1

        ball.x += xspeed * 1.4
        ball.y += yspeed * 1.4

    #------------SCREEN FILLS:-----------
    # Screen must be filled to prevent any weird trails
    # epilepsy mode:
        screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))  

    # ----------SCORES DISPLAY-----------
        scoreboardtext = font.render("Scoreboard", True, "white")
        p1text = font.render(str("Player 1: " + str(p1score)), True, "white")
        p2text = font.render(str("Player 2: " + str(p2score)), True, "white")
    
        scoreboardrect = scoreboardtext.get_rect(center=(width/2, 50))
        p1_rect = p1text.get_rect(center=(width/2 - 200, 80))
        p2_rect = p2text.get_rect(center=(width/2 + 200, 80))

        SpaceText = font.render("Press SPACE to return to the main menu", True, "white")
        Spacerect = SpaceText.get_rect(center=(width/2, height - 100))


    # draw the player paddles
        pygame.draw.rect(screen, "white", PlayerOne)
        pygame.draw.rect(screen, "white", PlayerTwo)
        pygame.draw.circle(screen, "white", ball.center, 10)

        screen.blit(p1text, p1_rect)
        screen.blit(p2text, p2_rect)
        screen.blit(scoreboardtext, scoreboardrect)
        screen.blit(SpaceText, Spacerect)

        pygame.display.update()
    # clock.tick : Frames per second
        clock.tick(300)

def endscreen():
    font = pygame.font.SysFont("Arial", 60)
    screen.fill("black")

    winner_text = font.render("Player __ wins!", True, "white")
    print(p1score)
    print(p2score)
    
    # Display the winner
    if p1score >= 10:
        winner_text = font.render("Player 1 wins!", True, "white")
    elif p2score >= 10:
        winner_text = font.render("Player 2 wins!", True, "white")

    winner_rect = winner_text.get_rect(center=(width/2, height + 600))
    
    # Display the final scores
    score_text = font.render(f"Final Score - Player 1: {p1score}, Player 2: {p2score}", True, "white")
    score_rect = score_text.get_rect(center=(width/2, height/2 + 50))

    SpaceText = font.render("Press SPACE to return to the main menu", True, "white")
    Spacerect = SpaceText.get_rect(center=(width/2, height - 100))

    screen.blit(winner_text, winner_rect)
    screen.blit(score_text, score_rect)
    screen.blit(SpaceText, Spacerect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                MainMenu()

def howtoplay():
    font = pygame.font.SysFont("Arial", 40)
    


MainMenu()
